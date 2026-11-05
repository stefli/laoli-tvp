---
name: tvp
description: >-
  When producing technology news/breakdown videos (9:16 true 2K default) with
  OpenDesign/HyperFrames—and finishing must one-shot deliver true 2K video
  1440×2560 (smooth spoken-news narration per narration_editorial + audible BGM
  at #music data-volume ~0.40) + dual 3:4 covers (Hypebeast B default/primary +
  mid yellow-capsule A alternate; master PNG + Douyin 1080×1440 JPG upload pack)
  + PUBLISH.md captions A/B/C + GitHub Release (2K asset) + Pages 看片/下载 links.
  Justin 2026-11-05: default 2K only; stop producing 4K unless explicitly asked.
  Viewport media priority: topic demo/short video first, then official stills with motion, else self-made graphics (§3c).
metadata:
  short-description: Professional 2K tech news video + covers + Pages/Release
---
# TVP (Tech Video Producer)（工业级真 2K 科技短视频与全套海报制作标准）

Produce high-density, authoritative technology news and breakdown videos for frontier models, hardware, and engineering breakthroughs. Generates studio-grade **true 2K（1440×2560）** artifacts without generic AI slop, irrelevant stock imagery, or fuzzy full-screen stretches.

**Justin 2026-11-05（画像/记忆向）**：**默认只出 / 只挂真 2K（1440×2560）**；**4K 停产**——除非 Justin 明文再要。成片发现路径 = GitHub Release 资产 + Pages 选题页「看片 / 下载」；聊天可附 B JPG + 短摘要（需要时也可附 2K 文件），不再靠聊天气泡硬塞大视频。

**一次性交付（硬约束）**：每条成片同一轮必须交齐——**真 2K 竖屏视频（含旁白+可听见的 BGM）+ 双 3:4 封面 A/B（2160×2880 母版 PNG + 抖音用 1080×1440 JPG 上传包）+ `PUBLISH.md` 文案 A/B/C**，并（见 §八）把封面+文案推上 `stefli/wechat` 选题库、**创建 Release 挂上 2K mp4**、在主题 Pages 写好看片/下载链接。缺视频音轨、缺封面母版或 JPG 上传包、缺文案、未入选题库、未挂 Release 2K / Pages 链接都不算完成。**旁白未过审稿标准也不算完成。**

---

## 一、铁律规约：UI 组件与排版绝对防偏规范 (Anti-Deviation Invariants)

### 1. 顶部主标题 = 全英文大写 + 一行中文对照（默认）
- **EN 主标 Mandatory**：全英文大写（Bahnschrift / DIN Alternate），两行或三行；首行白，强调色用 `<span>`。**禁止**把顶部主标改成中文。
- **坐标**：`.upper-section` `top: 220px, left/right: 64px`；`.headline` `font-size: 84px, line-height: 0.94`；`max-height` 约 **280px**（容纳中文对照）；收束须仍明显低于视口顶 `500px`。
- **中文对照 Mandatory（Justin 2026-10-29）**：每个 `.headline` 正下方加一行 `.headline-zh`（钩子/事实，约 **8–14 字**），帮助普通读者一眼读懂。
  ```css
  .headline-zh {
    margin-top: 14px;
    font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 44px;
    font-weight: 500;
    line-height: 1.2;
    letter-spacing: 0.02em;
    color: rgba(207, 216, 227, 0.92);
  }
  ```
- **禁止**：用第三行英文小标签/角标替代中文对照；禁止在 `0–220px` 再塞标签。

### 2. 废除顶部标题之上的小标签 / 角标
- 顶部 `0–220px` 必须留白；`top: 220px` 大标题是全屏第一个文字。

### 3. 中间赛博视口（默认必带框 · 对齐 Space Buddy 外框）
- **默认必须** Cyber Inspector Viewport（`top: 500px, height: 460px`），并完整保留：
  - 圆角边框 + 阴影（禁止 `border: none` / `border-radius: 0` / 无阴影直铺）
  - **四角包角** `.corner-bracket`（tl/tr/bl/br）
  - **顶栏** `::before` 46px + `.viewport-header`（dots + 短标签）
  - 媒体区 `.pagecam` / `.media` 从 **`top: 46px` / `height: calc(100% - 46px)`** 起裁，禁止 `inset:0` 盖住顶栏
- **禁止瞄准器 / 中央准星 HUD（Justin 2026-11-03）**：不要 `.hud-reticle`、十字线（`.cross-h` / `.cross-v`）、圆环准星、`.hud-focus-box`、`.hud-scan`，以及任何盖在画面正中的瞄准/扫描层。Space Bunny 旧成片里若有这些节点，**只学外框（包角+顶栏），不要抄瞄准器**。模板脚手架与 `examples/space_buddy_scene_s1.html` 均不得再含上述节点。
- 外框参考：`templates/standard_index.template.html` 的 MANDATORY SCENE SCAFFOLD；旧路径 `/workspace/minimax_space_bunny/index.html` 仅作外框对照，其中央 reticle **已废弃**。
- 仅当用户/选题**明确**说「去框/全幅」时才可去掉包角与顶栏；**LifeVal 多素材、新闻桌等不得自行去框**
- **未经要求不要挪** `top:500px` / `height:460px`。

### 3b. 每拍场景 HTML 必含（禁止只抄 CSS 忘节点）
从 `templates/standard_index.template.html` 里的 **MANDATORY SCENE SCAFFOLD** 复制，七拍各一份。`.central-viewport` 内**缺一不可**：
1. 四个 `.corner-bracket`（tl/tr/bl/br）
2. `.viewport-header`（短 EN 标签 + `.dots`）
3. `.pagecam`（或等价媒体层）包住 img/video —— CSS 已规定 `top:46px; height:calc(100% - 46px)`

**不要**再加：`.hud-layer` / `.hud-reticle` / `.hud-focus-box` / `.hud-scan`（瞄准器类）。

**反例**：
- `.central-viewport { border: none; border-radius: 0; box-shadow: none; }`（没框）
- `.pagecam { inset: 0; }` 盖住顶栏
- 场景里只有 `<div class="central-viewport"><video class="media"…>`，没有包角/顶栏节点
- 以「多素材/实景更爽」自行去框（须用户明文「去框」才可）
- 画面中央叠十字准星 / 圆环瞄准器 / focus-box / scanline（Justin：从技能删除，禁止再出）

黄金对照：**外框** = 模板脚手架；**不要**对照旧 Space Bunny 的中央瞄准器。


### 3c. 视口素材优先级（Justin 2026-11-05 · 硬约束）
中间 `.pagecam` **必须按下列顺序选材**，不得跳级用劣质替代：
1. **优先：主题官方/一手视频短片、产品 demo、发布会切片、案例对比 GIF/MP4**（能嵌就嵌；裁切进视口，保留可读关键内容）。这是吸引阅读的主画面，不是装饰。
2. **其次：官方截图、报告页、UI、评测图**——做成短动效（缓推/平移/切镜），**禁止七拍共用同一张静帧硬推 Ken Burns**。
3. **再不行：自创示意图/信息图**（须标注或能在 SOURCES 说清是自制），仍须每拍不同、服务旁白事实。
**禁止**：无主题相关的库存空镜、无关风景、纯抽象噪点当主画面；禁止「有静帧就交差」却跳过可下载的官方 demo。`SOURCES.md` 须写明每拍素材 URL 或自制说明；`STATUS.md` 勾选本条优先级。


### 4. 底部「两行中文解说 + 双指标卡」（默认；禁止卡墙）
- `.lower-section` 默认 **`top: 1048px`**（可在 `1008–1060` 微调）；内容底须 **&lt; 1360px**；**`1380–1920px` 平台控件区必须留白**。
- **解说 `.narrative`**：`font-size: 38px`，`line-height: 1.38`，`margin-bottom: 22px`；默认 **两行**（约 55–75 字），用信源里未上卡的硬事实补认知（教育价、核心数、预购日等）；仍须一眼能扫完，过长则收字，不靠加卡。
- **指标卡**：固定 **两张**（`1fr 1fr`）。**禁止**第三张卡/卡墙堆指标；多余事实进解说或 `PUBLISH.md`。
- 卡片自身 padding 等既有规格保持；未经要求不要改成全卡片底栏。

---

## 二、标准项目工程结构

```text
projects/<suite_name>/
├── assets/   # hero、gsap、manifest、music.wav、voice_01~07.wav、可选 demo 切片
├── index.html
├── gen_assets.py / gen_music.py
├── DESIGN.md / SOURCES.md
├── PUBLISH.md
├── posters/publish_test/
│   ├── cover_B_hypebeast_3_4.png     # 2160×2880 母版（现行默认主推）
│   └── cover_A_yellow_tape_3_4.png   # 备选黄胶囊
└── posters/douyin_upload/
    ├── cover_B_<slug>_1080x1440_q90.jpg  # 抖音等优先上传
    └── cover_A_<slug>_1080x1440_q90.jpg
```

模板：`templates/standard_index.template.html`（须含 `.headline-zh` 与上述底栏默认）。

---

## 三、通用 7 拍叙事（48s–53s）

Beat 01 Hook → 02 指标 → 03 官方/生态 → 04 机制 → 05 边界 → 06 涟漪 → 07 终局。

---

## 四、音频铁律（旁白 + BGM · 不可省略）

成片 **必须有音轨**：中文旁白 + 程序化 BGM。无声 / 只有画面 = 未完成。

### 旁白审稿（先于 TTS · 硬门禁）
完整标准见 [references/narration_editorial.md](references/narration_editorial.md)。摘要：
- **口播新闻稿**，不是书面摘要；出声读得顺才许进 TTS
- 每拍 **一句一意**，约 **28–42 字**；少用 `——` / 长顿号清单 / 「口径、结论、规格以」元话语
- **禁止**「大约 13 秒起」「00:13」「按章节」「以成片章节为准」——时间码只上画面/`PUBLISH`，旁白只说新闻事实
- **节奏**：新闻播报紧凑推进，拍间约 0.35–0.50s，不留思考空档
- **科技频道对照**：谁+干了什么先落地；禁架构黑话连发与拍间同义反复；画面解说不得比嘴更绕（详 narration_editorial §四甲）
- 每拍英文专名 **≤ 2**；能意译则意译；清单细节留给画面字卡或 `PUBLISH.md`
- TTS：`zh-CN-YunyangNeural`，rate 默认 **`+8%`～`+12%`（常用 +10%）**；密专名禁止硬上 `+14%`；`pitch=-1Hz`
- mastering 与抽听见 [references/audio_mastering.md](references/audio_mastering.md)
- `STATUS.md` 须勾选旁白审稿清单；未勾选 = 未完成
- 画面解说加长时，旁白仍按 28–42 字一句；**不要**把两行画面字原样塞进口播导致赶读

### 必交资产
- `assets/voice_01.wav` … `voice_07.wav`（每拍一条，与 7 beat 对齐）
- `assets/music.wav`（全片铺底）

### 旁白工艺
- 文案过审后再 TTS；`data-volume="1.0"`
- 事实只来自 `SOURCES.md`；数字默认阿拉伯数字

### BGM 音量（Justin：手机要听得到）
- 用工程 `gen_music.py` / skill `scripts/generate_music.py` 生成程序化立体声；**禁止**无授权商用曲库瞎贴
- HyperFrames `#music` **`data-volume` 默认 `0.40`**（允许 0.38–0.42）；**禁止** 0.20–0.22（太轻）与 0.65–0.70（Justin：太响）
- 旁白仍压过 BGM；未经要求不要改默认
- 与切点轻微同步；全程可辨，不挖到听不见

### 成片验收
- HyperFrames / `hf` 渲染须 **has audio**
- 交付前 `ffprobe` 确认存在音频流；抽听旁白**顺耳不吃力** + BGM 手机外放可辨

---

## 五、双 3:4 封面（母版 2160×2880 + 抖音上传 1080×1440 JPG）

每条成片默认并行出 A/B。细则与字号、**平台上传导出**以 [科技快播封面](sand-workflow:skill-1793030834146) 为准。

**现行默认主推（Justin 2026-11-02）= B · Hypebeast 潮牌**；A 黄胶囊仍必出作备选。聊天气泡与抖音上传**优先交 B JPG**。封面文案要有爆款钩子感（可稍绕口/反差），事实须真。

**封面/PUBLISH 中文标题 SEO（Justin 2026-11-05）**：当选题有可搜索的产品**品牌+型号**（如「腾讯混元Hy4」）时，**ZH 封面钩子与 PUBLISH A 开场 / B 一句话 / C 标题行须前置品牌+型号**，再接能力/反差钩子（例：`腾讯混元Hy4 / 第一次能看图还能点电脑`）。EN ALL-CAPS 主标可保持能力短语、与中文分流。标签继续含专名（如 `#混元` `#Hy4`）。勿只写能力线而丢掉可搜品名。

硬约束：一手实景底；EN ALL-CAPS + 大号中文副标；Hypebeast **无右侧圆章**；Puppeteer/CDP。

| 代号 | 风格 | 母版（存档） | 抖音上传包（必交） |
| --- | --- | --- | --- |
| **B** | **Hypebeast 潮牌（现行默认 · 主推）**；超大叠字 + 可选白底色块；无右侧圆章；底部中文爆款钩子 | `posters/publish_test/cover_B_hypebeast_3_4.png`（2160×2880 PNG） | `posters/douyin_upload/cover_B_<slug>_1080x1440_q90.jpg`（1080×1440 JPG q≈90，约 0.3–1.2MB） |
| **A** | **中间大字黄胶囊（备选）**（居中 `border-radius:999px` 黄胶带；EN ~240–264 / 副行 ~210–220；ZH ~168；禁止旧梯形胶带/顶部 masthead） | `posters/publish_test/cover_A_yellow_tape_3_4.png` | `posters/douyin_upload/cover_A_<slug>_1080x1440_q90.jpg` |

**上传铁律（Justin 2026-10-30）**：聊天气泡优先附 **B** JPG 上传包（再附 A）；**禁止**把 2K+ PNG 当抖音上传文件。勿经微信/QQ 转发后再传。选题库可继续放压缩 JPEG/PNG 母版。

---

## 六、自媒体发布文案（PUBLISH.md A/B/C）

同一轮交付。[references/publish_captions.md](references/publish_captions.md)。

---

## 七、标准范本参考

- [references/narration_editorial.md](references/narration_editorial.md) ← **旁白审稿**
- [references/case_study_kling.md](references/case_study_kling.md)
- [references/vertical_safe_zones.md](references/vertical_safe_zones.md)
- [references/cover_design.md](references/cover_design.md)
- [references/audio_mastering.md](references/audio_mastering.md)
- [references/publish_captions.md](references/publish_captions.md)
- [references/render_pipeline.md](references/render_pipeline.md)

---

## 八、一次性交付清单（Done Definition）

**默认成片规格（Justin 2026-11-05）**：**真 2K 竖屏 1440×2560 only**。**停止生产 4K**（勿渲染/勿上传/勿在 Pages 链 4K），除非 Justin 本条明文再要。

1. **旁白审稿通过**（narration_editorial 清单已勾进 STATUS）
2. **视频**：竖屏 **真 2K（1440×2560）** + **旁白 + 可听见的 BGM**（`#music`≈0.40）；抽听顺耳；画面含 **EN 主标 + `.headline-zh` 中文对照** + **两行解说 + 双卡**；视口素材遵守 **§3c 优先级**（主题 demo/短片 → 截图动效 → 自创图）。输出路径约定：`outputs/<suite>_2k.mp4`。
3. **封面**：B（Hypebeast 主推）+ A（黄胶囊备选）：**母版 PNG** + **抖音 1080×1440 JPG 上传包**（缺 JPG = 未完成）；聊天气泡优先附 B
4. **描述**：`PUBLISH.md` A/B/C
5. **信源**：`SOURCES.md`
6. **GitHub 选题库 Pages（管理 + 发现）**：把封面 A/B（可压 JPEG）+ `PUBLISH.md` + **可一点复制的 `index.html`（A/B/C 各带复制按钮）** 推到 `stefli/wechat` 的 `public/tvp/<slug>/`，更新总览 `public/tvp/index.html` 与 `catalog.json`（可加 `video_2k` / `release` 字段）；Pages 入口 [https://stefli.github.io/wechat/tvp/](https://stefli.github.io/wechat/tvp/)，主题页 `/tvp/<slug>/`。主题页须有醒目 **「看片 / 下载」**（2K 直链；可选 HTML5 `<video>` 播 Release CDN）。**国内加速链（Justin 2026-11-05 · 默认必挂）**：主题页下载区除官方 GitHub Release asset URL（标 **原链**）外，**同时**提供至少两条国内加速下载：默认主按钮 **加速下载** = `https://ghfast.top/` + 完整 GitHub Release asset URL；备用 **备用加速** = 另一代理（现行默认 `https://ghproxy.net/` + 同一完整 asset URL）。标签须写清「加速下载 / 备用加速 / 原链」。`<video src>` 可优先试 ghfast；播不出则回退官方 GitHub 并依赖下载按钮。**代理为第三方、可能失效或换域名——永远保留官方 GitHub 原链。****git 树禁止提交大 mp4 进 `public/tvp/`**——成片只走 Release 资产。例外：Justin 明文要求的手机临时包，用完常删（旧规仍在）。
7. **GitHub Release（成片托管）**：在 `stefli/wechat` 为该 slug 建 Release（tag 例 `tvp-<slug>`），**只挂 2K mp4** 为 asset；把 asset URL 写进主题页 + catalog，并按上条挂上 **ghfast 加速下载 + 备用代理 + 原链**。本地 `gh release create`（auth 已在 box 则直接用）；**优先本地 git，勿为推仓开 Cursor 云端**。
8. 经捕手转交时回：2K 路径 + Release URL + asset URL + Pages 链接；聊天气泡优先附 **B JPG** + 短摘要（需要时可附 2K 文件）。**视频发现主路径 = Pages 看片/下载**，减轻聊天复制大文件摩擦。

**STATUS.md 备注模板（画像向）**：写明 `Composition/Deliverable: 1440×2560 true 2K · no 4K unless Justin asks`；勾旁白审稿；记 `Release:` 与 `Pages:` URL。

缺旁白审稿 / 旁白吃力 / 缺音轨 / BGM 过小听不见 / 缺封面母版或 **缺抖音 JPG 上传包** / 缺文案 / 缺中文对照 / **视口未按 §3c 优先嵌主题 demo（有官方短片却只用静帧）** / 未入选题库 / **未建 Release 或未挂 2K / Pages 无看片下载或无国内加速链（加速+备用+原链）** = 未完成。

## 九、导出给 WorkBuddy / Codex / Gemini（便携包）

装包时须**整夹**复制 `tvp/`、`科技快播封面/`、`tvp-dh/`（含 `templates/`、`references/`、`scripts/`），不要只丢一个 `SKILL.md`。

常见「效果差很多」根因：
1. **只索引了 SKILL 摘要，没读 template 脚手架** → 模型自造无包角直铺画面（像 2026-11 新闻桌回归）
2. **旧包（≤2026-11-02）** 未写死「默认必带框」与场景节点清单
3. 封面技能仍指向本机绝对路径（如 `/workspace/opus_video_demos/...`）而包内已有 `templates/cover_*.html` —— 便携包必须用相对路径
4. 未按默认交付 **真 2K（1440×2560）**（却去交/挂 4K，或只剩 1080p），或 BGM 音量被压到 ~0.2，或旁白跳过 YunyangNeural / 审稿；或忘了 Release+Pages 看片链接
5. 跳过可拿到的主题 demo/短片，七拍复用同一张静帧 Ken Burns（违反 §3c）

验收：任意一拍截帧应能看到**顶栏字 + 四角包角 + 圆角描边**；对不上就按 §3 / §3b 重出，不要交付。
