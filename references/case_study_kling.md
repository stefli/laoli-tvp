# Case Study: 可灵 Kling 4.0 API 滚动开放 4K 科技快播

> **Layout note (2026-11-02):** If any coordinates in this case study conflict with the current `tvp/SKILL.md` 铁律, **SKILL.md wins**. Current defaults require `.headline-zh` under each EN headline, `.lower-section` near **`top: 1048px`** (tune 1008–1060), **exactly 2** metric cards (`1fr 1fr`), and platform UI band **`1380–1920` empty**.

Source project: `outputs/tech_video_producer_repo/projects/kling_4_api_bulletin`

## 为什么 Kling 4.0 是官方黄金范式（The Gold Standard）
Kling 4.0 API 播报（53.0s，原生 4K 2160×3840）代表了 `tech-video-producer` 现行生产力巅峰：
- **单文件自包含架构（Single-File Composition）**：摒弃多组件嵌套带来的碎片化与路径陷阱，全部场景、CSS 变量、硬件角标、数据漏斗与 GSAP 切割均收敛在单份 `index.html`。
- **双 >=40px 呼吸间距与 540px 底部净空**：大标题（Zone 1）到视口（Zone 2）留有 40-55px 净空，视口到底部遥测（Zone 3）留有 48px 净空，下方在 1250px 提前收束，给短视频平台 UI 留出超过 130px 冗余。
- **画中画动态 Retension Hook（PiP Live Demo）**：开篇 0.0s 拒绝静止黑屏，主视口右下角嵌入 340×192px 动态视频窗，打上 `● LIVE DEMO` 青绿指示点，第一秒即锁住完播率。
- **真机 Chrome 无损海报流水线**：拒绝 PIL 脚本画图，全部由 HTML 模板通过 Chrome Headless 直接生成 2160×2880、2160×3840、2160×2160 与 6480×3840 无损三联画板。

---

## 目录标准工程结构（每个视频项目的必须组成）

```text
projects/<suite_name>/
├── assets/
│   ├── <suite_name>_hero.jpg       # 官方一手实景主图 / Key Art
│   ├── gsap.min.js                 # 本地嵌入的 GSAP 动画引擎
│   ├── manifest.json               # 7 拍 TTS 文本、时长与音轨清单
│   ├── music.wav                   # 纯代码合成的程序化脉冲 BGM
│   ├── voice_01.wav ~ 07.wav       # 6 级广播母带处理后的旁白音频
│   └── (可选 demo 视频切片)        # 画中画或视口回放真实视频
├── index.html                      # 单文件 HyperFrames 4K 原生工程
├── gen_assets.py                   # 并发 TTS 请求与广播滤波链母带脚本
├── gen_music.py                    # 128 BPM 程序化脉冲合成脚本
├── DESIGN.md                       # 设计与视听分镜头执行台账
└── SOURCES.md                      # 一手信源、能力边界与事实核验报告
```

---

## 核心组件与 CSS 规范（直接复用）

### 1. 颜色与排版变量
```css
:root {
  --ink: #05070d;
  --paper: #f7f9fc;
  --ash: #cfd8e3;
  --gray: #94a3b8;
  --brand: #3b82f6;
  --cyan: #00f2fe;
  --yellow: #ffe600;
  --red: #ef4444;
  --teal: #10b981;
  --border: rgba(148, 163, 184, 0.28);
  --display: "Bahnschrift", "DIN Alternate", sans-serif;
  --cjk: "Microsoft YaHei", "PingFang SC", sans-serif;
  --mono: "Cascadia Mono", "Consolas", monospace;
}
```

### 2. 响应式 3 区域绝对定位（双 >=40px 净空）
```css
/* Zone 1: Headline Zone */
.upper-section {
  position: absolute; top: 220px; left: 64px; right: 64px; max-height: 240px; z-index: 20;
}
.headline {
  font-family: var(--display); font-size: 84px; font-weight: 700; line-height: 0.94;
  letter-spacing: -0.02em; text-transform: uppercase; color: #fff;
}

/* Zone 2: Central Viewport (top: 500px, height: 460px, Gap 1 = 40-55px) */
.central-viewport {
  position: absolute; top: 500px; left: 64px; right: 64px; height: 460px;
  background: linear-gradient(180deg, rgba(17, 24, 39, 0.96) 0%, rgba(9, 13, 22, 0.98) 100%);
  border: 1px solid var(--border); border-radius: 12px;
  box-shadow: 0 25px 70px rgba(0,0,0,0.92), 0 0 40px rgba(59,130,246,0.12);
  overflow: hidden; z-index: 10;
}

/* Zone 3: Lower Telemetry & Specs (top: 1008px, Gap 2 = 48px) */
.lower-section {
  position: absolute; top: 1008px; left: 64px; right: 64px; z-index: 20;
}
.narrative {
  font-size: 38px; line-height: 1.42; font-weight: 350; color: var(--ash); margin-bottom: 18px;
}
.spec-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.spec-item {
  background: rgba(15,23,42,0.92); border: 1px solid var(--border); padding: 14px 20px; border-radius: 6px;
}
.spec-item .label {
  display: block; margin-bottom: 5px; font-size: 21px; font-family: var(--mono); color: var(--gray); text-transform: uppercase;
}
.spec-item .val {
  font-family: var(--display); font-size: 50px; font-weight: 700; color: var(--paper); line-height: 1;
}
```

### 3. 数据漏斗行（Funnel Row）与终端代码行（Term Line）
视口内部必须根据内容类型展示模块化数据行：
- **Funnel Row**：左侧 5px 色块，右侧大字指标与说明；
- **Term Line**：代码等宽字体，高亮 `[OK]`、`[WARN]`、`[ERR]`；
- **Media / PiP**：视口内直接回放 16:9 主画，右下角可选悬浮画中画。

---

## 7 拍通用叙事模板（从 Kling 4.0 抽象）

| 拍次 (Beat) | 窗口区间 | 叙事功能 | 画面与视口呈现 | 声音设计 |
|---|---|---|---|---|
| **Beat 01** | `0.0 - 7.5s` | **破局与突发 (The Hook)** | 官方 Key Art / Demo 视频立即播放；大标题亮起；画中画指示灯脉冲 | Sub-bass drop + 脉冲底鼓进场 |
| **Beat 02** | `7.5 - 15.0s` | **核心突破与关键指标** | 数据漏斗排布（指标大幅跃升、速度对比、关键规格） | 16分音符贝斯推进 |
| **Beat 03** | `15.0 - 22.5s` | **官方架构与生态动作** | 架构图 / 平台接入方 / 官方接口调用展示 | 镜头切点 Whoosh + 晶体音 |
| **Beat 04** | `22.5 - 30.0s` | **机制深潜与硬核剖析** | 多角度推演 / 运行逻辑拆解 / 真实协议流水线 | 稳定中频律动 |
| **Beat 05** | `30.0 - 37.5s` | **能力边界与失效条件** | 警示黄色/红色高亮（如未支持音频、算力瓶颈、协同短板） | 警报提示微音 (Alarm beep) |
| **Beat 06** | `37.5 - 45.0s` | **全球影响与行业涟漪** | 竞品对比矩阵 / 区域受害或采用范围 / 产业链共振 | 律动增强，蓄力推升 |
| **Beat 07** | `45.0 - 53.0s` | **终局定性与战略考题** | 终极定性标牌居中；权威信源汇总行；结论句升华 | 尾声合成器氛围淡出至黑 |

---

## 自动化海报装配（render_all_series_masters.py）

在 `posters/` 目录下：
1. 编写 `templates/<slug>_photo_3_4.html` 与 `templates/<slug>_photo_9_16.html`；
2. 在 `posters/scripts/render_all_series_masters.py` 注册套件；
3. 运行脚本，自动输出 3:4、9:16、1:1 方图与 6480×3840 顶部对齐三联主板！
