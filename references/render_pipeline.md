# HyperFrames 真 2K 渲染与交付指南

**Justin 2026-11-05**：默认成片 = **真 2K 竖屏 1440×2560 only**。**4K 停产**（除非 Justin 明文再要）。平台上传与 Pages/Release 托管都走 2K。

## 一、为何默认真 2K（而不是 1080p / 4K）

- **1080×1920**：国内平台二次压缩后细线/字易糊，不作为成片规格。
- **2160×3840（4K）**：文件大、复制摩擦高；Justin 已要求默认停产，不再作为一次性交付物，也不挂 Release。
- **1440×2560（真 2K）**：体积可控（常见数 MB～十余 MB），观感明显优于 1080p，适合 Release CDN + Pages「看片 / 下载」。

## 二、标准导出（交付物只有 `_2k.mp4`）

HyperFrames CLI 预设目前是 `portrait`（1080×1920）与 `portrait-4k`（2160×3840），**没有**整数 DPR 的 `portrait-2k`。推荐路径：

```bash
# 1) 门禁
npx hyperframes lint
npx hyperframes check

# 2) 需要超采样画质时，可短暂用 portrait-4k 捕获，再立刻下采样为交付 2K，并删除 4K
npx hyperframes render . -o outputs/<suite>_4k.mp4 --resolution=portrait-4k --quality=delivery
ffmpeg -y -i outputs/<suite>_4k.mp4 \
  -vf scale=1440:2560:flags=lanczos \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart \
  -c:a aac -b:a 192k \
  outputs/<suite>_2k.mp4
rm -f outputs/<suite>_4k.mp4   # 4K 不是交付物

# 验收
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 outputs/<suite>_2k.mp4
# 期望：1440,2560
```

若 Justin **明文**要 4K，才保留 `outputs/<suite>_4k.mp4` 并另议是否上 Release（默认仍只挂 2K）。

### 关键参数
- `--resolution=portrait-4k`：仅作中间超采样（可删）；**不要**把该文件当 Done。
- `--quality=delivery`：交付级 CRF / 色彩。
- 最终对外：**只有** `outputs/<suite>_2k.mp4`（1440×2560）+ Release asset + Pages 链接。

## 三、渲染前必经的两步门禁

```bash
npx hyperframes lint
npx hyperframes check
```

只有在 check 完全通过的前提下，才执行正式渲染。

## 四、托管

- `gh release create tvp-<slug> outputs/<suite>_2k.mp4 …`（`stefli/wechat`）
- 主题页 `public/tvp/<slug>/` 写「看片 / 下载」直链（可选 `<video>`）
- **禁止**把 mp4 提交进 `public/tvp/` git 树
