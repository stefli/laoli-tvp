# 科技快播封面设计（现行锁定 A/B + 抖音上传）

> **Version 2026-11-02 final.** 科技快播 / TVP 成片封面以本节锁定的 **A/B 发布对** 为准。完整字号与九宫格流程见封面技能 `科技快播封面/SKILL.md`。

---

## 1. 现行默认主推：双 3:4 发布对（必交）

每条成片同一轮交 **B + A**（与 4K 视频、`PUBLISH.md` 同批）。

| 代号 | 风格 | 角色 | 母版路径 | 要点 |
| --- | --- | --- | --- | --- |
| **B** | **Hypebeast 潮牌** | **现行默认 · 主推** | `posters/publish_test/cover_B_hypebeast_3_4.png`（2160×2880 PNG） | 顶部超大 EN 叠字 + 可选白底色块；**无右侧圆章**；底部大号中文爆款钩子；聊天气泡与抖音**优先交 B** |
| **A** | **中间大字黄胶囊** | **备选 · 仍必出** | `posters/publish_test/cover_A_yellow_tape_3_4.png` | 居中 `border-radius:999px` 黄胶带胶囊；EN ~240–264 / 副行 ~210–220；ZH ~168；**禁止**梯形 `clip-path`、顶部 masthead 黄条 |

硬约束（两边共用）：

1. 底图 = 一手实景/官片静帧，禁止纯色空底或 flat logo 冒充照片。
2. 文案默认两层：英文 ALL-CAPS 主标 + 中文一级副标（可两行口语钩子）；不要数据卡墙、角标堆。
3. 画布 **2160×2880**；HTML + Puppeteer/CDP 截图（不用 PIL 手绘字）。
4. 九宫格探索阶段不要覆盖已锁正式封面，除非用户点名替换。
5. 封面文案可有爆款钩子感，事实必须真。

参考 HTML 模板（技能包内）：

- `科技快播封面/templates/cover_B_hypebeast.html`
- `科技快播封面/templates/cover_A_yellow_tape.html`

---

## 2. 抖音 / 短视频上传包（硬）

存档母版保持 **2160×2880 PNG**。**禁止**把 2K+ PNG 直接当抖音上传文件。

| 用途 | 规格 | 路径约定 |
| --- | --- | --- |
| 存档 / 选题库母版 | 2160×2880 PNG（3:4） | `posters/publish_test/cover_{B\|A}_*_3_4.png` |
| **抖音等直接上传** | **1080×1440 JPG**，sRGB，质量 **≈90**，`subsampling=0`（4:4:4），约 **0.3–1.2MB** | `posters/douyin_upload/cover_{B\|A}_<slug>_1080x1440_q90.jpg` |

导出规则：

1. 从母版 **LANCZOS** 缩到 1080×1440 再存 JPG。
2. 聊天气泡优先附 **B JPG**，再附 A；勿经微信/QQ 转发后再传。
3. 可选 1080×1920 仅当用户点名；抖音主页卡片默认优先 3:4 的 1080×1440。

```python
from PIL import Image
im = Image.open("posters/publish_test/cover_B_hypebeast_3_4.png").convert("RGB")
im.resize((1080, 1440), Image.Resampling.LANCZOS).save(
    "posters/douyin_upload/cover_B_<slug>_1080x1440_q90.jpg",
    "JPEG", quality=90, optimize=True, subsampling=0,
)
```

---

## 3. B / A 速查规格

### B · Hypebeast（主推）

- 布局：顶部超大 EN 叠字栈 + **底部**大号中文钩子
- EN：Bebas / Anton / Impact；首行约 260–300px，次行约 220–260px；行高 ~0.78；强描边/投影
- 可选第三行白底黑字色块（约 140–180px）+ 色块投影（如 `#cc785c`）
- ZH：Noto Sans CJK SC 粗体约 100–120px；约 bottom 140–180px
- **禁止**：右侧圆形 sticker

### A · 中间黄胶囊（备选）

- 布局：整块文字垂直+水平居中（flex center）
- 黄胶带：`background:#ffe600`；**`border-radius:999px`**；`clip-path:none`；约 `rotate(-1.5deg)`
- EN：Oswald/Impact ~240–264px；副行 ~210–220px
- ZH：约 168px；白字强描边；胶带与 ZH 间距约 64–80px
- **禁止**：梯形胶带端、顶部 masthead 黄条、旧 LaoliCover 半身式排版冒充 A

---

## 4. Legacy — do not use for 科技快播 covers

下列内容来自早期小红书多层级色块 / 梯形胶带 / 顶部 masthead / 三联切割板实验，**不再作为科技快播封面推荐做法**（仅留档防误用）：

- 四级字号色块墙（荧光黄/火焰红多层板）作为默认封面架构
- 梯形胶带 `clip-path: polygon(...)` 或不规则 skew 胶带端
- 顶部品牌 Masthead 黄条 + 多段色块标题栈
- 默认出 6480×3840 三联切割主板 / 多格式同步母版作为主交付

若用户明确点名「旧杂志封面 / 三联板」再考虑，否则一律走上文锁定的 **B Hypebeast + A 黄胶囊**。
