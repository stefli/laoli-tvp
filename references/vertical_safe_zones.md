# 9:16 Vertical Safe Zones & Responsive 3-Zone Architecture

Designed for mobile short-video feeds (TikTok, Douyin, WeChat Channels, YouTube Shorts, Xiaohongshu).

## The Problem: Multi-Line Headline Collision

In earlier versions, rigid absolute coordinates (`.upper-section top:220px`, `.central-viewport top:450px`, `.lower-section top:1036px`) assumed headlines never exceed 2 lines. When an editorial title wrapped to **3 lines**, it collided with the central viewport header, while leaving excessive empty space at the bottom (between 1280px and 1400px).

## Spatial Coordinate Map (1080 × 1920)

```text
0px    ┌───────────────────────────────────────────────┐
       │   TOP SAFE ZONE (0 - 220px)                   │ <-- Leave completely empty
       │   [Platform Follow / Search / Back Controls]  │
220px  ├───────────────────────────────────────────────┤
       │   DYNAMIC GOLDEN STAGE (220 - 1380px)         │ <-- 1160px Available Canvas
       │                                               │
       │   ┌───────────────────────────────────────┐   │
       │   │ Zone 1: HEADLINE (220 - 460px)        │   │ <-- 88-96px (1-2 lines) or 76-84px (3 lines)
       │   │ [Auto-scaling, line-height: 0.94]     │   │
       │   ├───────────────────────────────────────┤   │
       │   │ Zone 2: CENTRAL VIEWPORT (480 - 980px)│   │ <-- 480-500px Height (Clamped aspect)
       │   │ [16:9 / 18:9 Cyber Inspector Card]    │   │
       │   ├───────────────────────────────────────┤   │
       │   │ Zone 3: TELEMETRY & SPECS (1000-1360px│   │ <-- 38-40px Narrative + 52px Specs
       │   │ [Clamped by 1380px Safe Ceiling]      │   │
       │   └───────────────────────────────────────┘   │
1380px ├───────────────────────────────────────────────┤
       │   BOTTOM SAFE ZONE (1380 - 1920px)            │ <-- Leave completely empty (540px Clearance)
       │   [Creator Handle & Caption Rail]             │
       │   [Like / Comment / Share / Collect Bar]      │
       │   [Rotating Audio Disc & Scrub Bar]           │
1920px └───────────────────────────────────────────────┘
```

## Standard Responsive 3-Zone Rules

To ensure robust rendering across 1-line, 2-line, or 3-line headlines without overlap:

### 1. Unified Golden Frame Container
Encapsulate each scene inside an adaptive container anchored from `top: 220px` to `bottom: 540px` (or `height: 1160px`), using vertical flexbox or calibrated proportional offsets:

```css
/* Option A: Vertical Flex Flow (Zero Collision Guarantee) */
.scene-stage {
  position: absolute;
  top: 220px;
  left: 64px;
  right: 64px;
  height: 1160px; /* 220px to 1380px */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Zone 1: Headline */
.headline {
  font-family: var(--display);
  font-weight: 700;
  line-height: 0.94;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  /* 1-2 lines: 92px - 96px; 3 lines: 78px - 82px */
  font-size: clamp(76px, 8vw, 96px);
}

/* Zone 2: Central Viewport */
.central-viewport {
  position: relative;
  width: 100%;
  height: 500px; /* Calibrated from 556px to afford 3-line headline headroom */
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

/* Zone 3: Telemetry & Specs */
.lower-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.narrative {
  font-size: 38px;
  line-height: 1.4;
  font-weight: 400;
  color: var(--ash);
}
.spec-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.spec-item {
  background: rgba(15, 23, 42, 0.92);
  border: 1px solid var(--border);
  padding: 14px 20px;
  border-radius: 6px;
}
.spec-item .val {
  font-family: var(--display);
  font-size: 50px;
  font-weight: 700;
  line-height: 1.0;
}
```

### 2. Proportional Calibrations for Absolute Layouts
If using absolute positioning across GSAP transitions:

| Element / Boundary | Old 20px (Cramped / Collision-Prone) | Mandatory >= 40px Breathing Standard | Measured In-Engine Benefit |
| :--- | :--- | :--- | :--- |
| **Headline Zone** | `220px - 440px` (104px font) | **`220px - 460px`** (`84px`, line-height `0.94`) | Accommodates 1, 2, or 3 full lines, ends at Y=445-460px |
| **Gap 1 (Top Clearance)** | `15px - 20px` (optical collision) | **`40px - 55px` Absolute Net Gap** | Viewport top at **`500px`**, zero visual crowding |
| **Central Viewport** | `440px - 996px` (556px height) | **`500px - 960px`** (**`460px`** height) | 16:9/18:9 framed monitor, 4 corner HUD brackets |
| **Gap 2 (Bottom Clearance)**| `22px - 26px` (dense crowding) | **`48px - 50px` Absolute Net Gap** | Viewport bottom at 960px -> Telemetry top at **`1008px`** |
| **Lower Telemetry Zone** | `1030px - 1320px` | **`1008px - 1250px`** (Narrative 38px, Specs 52px) | Finishes at ~1250px; leaves massive **130px+ bottom buffer** above 1380px |

This calibration guarantees:
1. Even with **3 full uppercase headline lines**, the title never collides with the central viewport header (`220 + 240 = 460px < 480px`).
2. The central viewport retains a commanding 500px presence with sharp 16:9 media scaling.
3. The bottom section terminates comfortably around `1320px`, completely respecting the `1380 - 1920px` platform safe zone without bottom crowding.
