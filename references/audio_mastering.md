# Broadcast Audio Mastering & Procedural Synth Score

## Voiceover Generation Pipeline

Use `zh-CN-YunyangNeural` with **`rate=+8%` to `+12%`** (default **`+10%`**) and `pitch=-1Hz` for comfortable broadcast delivery. Use `+14%` only on very short, low-jargon hook lines. Dense proper-noun scripts must NOT stay at +14%.

**Script quality gates first:** follow [narration_editorial.md](narration_editorial.md). Bad copy cannot be fixed by mastering.

```python
import asyncio, edge_tts

async def gen_one(text, out_mp3, rate="+10%"):
    c = edge_tts.Communicate(text, "zh-CN-YunyangNeural", rate=rate, pitch="-1Hz")
    await c.save(out_mp3)

async def gen_all_parallel(lines):
    # 5x faster: concurrently dispatches all chunks
    await asyncio.gather(*(gen_one(text, f"raw_{idx}.mp3") for idx, text in lines))
```

## Studio Mastering Filter Chain (FFmpeg)

Apply this exact filterchain to transform raw TTS into a high-authority studio broadcast voice:

```bash
ffmpeg -y -i raw.mp3 \
  -af "highpass=f=80,equalizer=f=220:t=q:w=1.2:g=1.8,equalizer=f=3300:t=q:w=1.2:g=2.2,equalizer=f=8500:t=q:w=1.0:g=1.5,acompressor=threshold=-18dB:ratio=3:attack=10:release=100,loudnorm=I=-16:TP=-1.5:LRA=7" \
  -ar 48000 -ac 2 mastered.wav
```

- `highpass=f=80`: Removes sub-audible rumble.
- `equalizer=f=220`: Adds warm chest resonance.
- `equalizer=f=3300`: Boosts consonantal articulation and speech intelligibility.
- `equalizer=f=8500`: Introduces studio "air" sheen.
- `acompressor`: Smooths peak dynamic range for a dense, radio-ready delivery.
- `loudnorm=I=-16`: Standardizes to international EBU R128 loudness.

## 48-Second Pulse Synthesizer Script

Use `scripts/generate_music.py` to synthesize procedural stereo tracks with beat-synchronized kicks, shimmers, drones, and transitional cut whooshes.

---

## BGM Mix Level (Justin preference)

Phone speakers bury quiet beds. Default HyperFrames music bus:

| Track | `data-volume` | Notes |
| --- | --- | --- |
| `#music` BGM | **0.38 – 0.42** (default **0.40**) | Audible under VO on phone; Justin reverted from 0.68 (too loud) |
| `#voiceN` narration | **1.0** | Always sit above BGM |

Do not duck BGM to near-silence. Keep default **0.40**; do not use 0.20–0.22 (too quiet) or 0.65–0.70 (Justin: too loud). Whoosh/hit accents may briefly peak higher inside `music.wav` itself.
