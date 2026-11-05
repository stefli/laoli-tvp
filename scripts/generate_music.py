import math
import wave
from pathlib import Path

import numpy as np


SR = 44100
DURATION = 48.0
BEAT = 60.0 / 126.0
rng = np.random.default_rng(20261013)


def envelope(length: int, attack: float, decay: float) -> np.ndarray:
    t = np.arange(length) / SR
    a = np.clip(t / max(attack, 1e-4), 0.0, 1.0)
    d = np.exp(-t / max(decay, 1e-4))
    return a * d


def add(signal: np.ndarray, sample: np.ndarray, start: float, gain: float = 1.0) -> None:
    begin = int(start * SR)
    end = min(len(signal), begin + len(sample))
    if begin < len(signal) and end > begin:
        signal[begin:end] += sample[: end - begin] * gain


def kick() -> np.ndarray:
    n = int(0.22 * SR)
    t = np.arange(n) / SR
    freq = 62.0 * np.exp(-t * 15.0) + 36.0
    phase = 2 * np.pi * np.cumsum(freq) / SR
    body = np.sin(phase) * np.exp(-t * 17.0)
    click = rng.normal(0, 1, n) * np.exp(-t * 100.0)
    return 0.9 * body + 0.12 * click


def hat() -> np.ndarray:
    n = int(0.05 * SR)
    t = np.arange(n) / SR
    noise = np.diff(np.concatenate(([0.0], rng.normal(0, 1, n))))
    return noise * np.exp(-t * 90.0) * 0.13


def bass_note(freq: float, length: float) -> np.ndarray:
    n = int(length * SR)
    t = np.arange(n) / SR
    saw = 2.0 * ((t * freq) % 1.0) - 1.0
    sub = np.sin(2 * np.pi * freq * t)
    return (0.34 * saw + 0.66 * sub) * envelope(n, 0.008, 0.22)


def glass_note(freq: float, length: float) -> np.ndarray:
    n = int(length * SR)
    t = np.arange(n) / SR
    tone = (
        np.sin(2 * np.pi * freq * t)
        + 0.45 * np.sin(2 * np.pi * freq * 2.01 * t)
        + 0.2 * np.sin(2 * np.pi * freq * 3.99 * t)
    )
    return tone * envelope(n, 0.015, 0.5) * 0.12


def whoosh(length: float) -> np.ndarray:
    n = int(length * SR)
    t = np.arange(n) / SR
    noise = np.convolve(rng.normal(0, 1, n), [1.0, -0.94], mode="same")
    return noise * (np.clip(t / length, 0.0, 1.0) ** 2.2) * 0.16


def main() -> None:
    total = int(DURATION * SR)
    left = np.zeros(total)
    right = np.zeros(total)
    kick_sample = kick()
    hat_sample = hat()
    pattern = [55.0, 55.0, 73.42, 65.41, 49.0, 55.0, 82.41, 73.42]
    glass = [440.0, 493.88, 587.33, 659.25, 493.88, 440.0, 392.0, 493.88]

    beat_index = 0
    time = 0.0
    while time < DURATION:
        add(left, kick_sample, time, 0.7)
        add(right, kick_sample, time, 0.7)
        add(left, hat_sample, time + BEAT / 2, 0.9)
        add(right, hat_sample, time + BEAT / 2, 0.7)
        note = bass_note(pattern[beat_index % len(pattern)], BEAT * 0.86)
        add(left, note, time, 0.16)
        add(right, note, time + 0.004, 0.16)
        if beat_index % 2 == 1:
            shimmer = glass_note(glass[beat_index % len(glass)], BEAT * 1.5)
            add(left, shimmer, time + BEAT * 0.5, 0.45)
            add(right, shimmer, time + BEAT * 0.52, 0.5)
        beat_index += 1
        time += BEAT

    t = np.arange(total) / SR
    drone = (
        np.sin(2 * np.pi * 36.71 * t)
        + 0.32 * np.sin(2 * np.pi * 55.0 * t)
        + 0.14 * np.sin(2 * np.pi * 110.0 * t)
    )
    drone *= 0.042 * (0.72 + 0.28 * np.sin(2 * np.pi * 0.09 * t))
    left += drone
    right += np.roll(drone, 160)

    for cut in (6.8, 13.6, 20.6, 27.6, 34.0, 40.8):
        add(left, whoosh(0.55), cut - 0.4, 0.9)
        add(right, whoosh(0.55), cut - 0.4, 0.8)
        add(left, kick_sample, cut, 0.35)
        add(right, kick_sample, cut, 0.35)

    stereo = np.stack((left, right), axis=1)
    stereo = np.tanh(stereo * 1.2)
    peak = np.max(np.abs(stereo))
    stereo = stereo / max(peak, 1e-9) * 0.78

    out = Path("outputs/gemini_argon/assets/music.wav")
    out.parent.mkdir(parents=True, exist_ok=True)
    pcm = (stereo * 32767).astype(np.int16)
    with wave.open(str(out), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SR)
        wav.writeframes(pcm.tobytes())
    print(out)


if __name__ == "__main__":
    main()
