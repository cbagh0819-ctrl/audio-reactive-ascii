# 🌌 Audio-Reactive 3D Hologram & Ultra-HD ASCII Visualizer

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-00f3ff?style=for-the-badge&logo=github)](https://cbagh0819-ctrl.github.io/audio-reactive-ascii/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Creator](https://img.shields.io/badge/Created%20By-Chandan%20Bagh-ff0055?style=for-the-badge&logo=github)](https://github.com/cbagh0819-ctrl)
[![Tech: Pure Web Standards](https://img.shields.io/badge/Tech-HTML5%20%7C%20Web%20Audio%20%7C%20Canvas2D-brightgreen?style=for-the-badge)]()

> A real-time, zero-dependency procedural graphics and video synthesizer featuring an interactive **3D Hologram Depth Field (2.5D Tilt & Orbit)**, **Ultra-HD Unicode Braille 2×4 Dot Matrices ($8\times$ spatial resolution)**, **Bayer halftone dithering**, **pixel-accurate True Color RGB sampling**, and **music beat-synced chromatic aberration**.

🔗 **Try the Live Visualizer directly in your browser:**  
👉 **[https://cbagh0819-ctrl.github.io/audio-reactive-ascii/](https://cbagh0819-ctrl.github.io/audio-reactive-ascii/)**

---

## ✨ Features & Architecture

### 1. 🌌 3D Hologram Depth Field (2.5D Tilt & Orbit)
- **Mouse Drag Orbit & Tilt**: Click and drag across the canvas to rotate the camera around the live ASCII plane in full 3D perspective ($Yaw \times Pitch$).
- **Luminance $Z$-Depth Extrusion**: Every character cell / Braille block is elevated along the Z-axis proportionally to its brightness. Bright highlights float toward the camera into a holographic point cloud.
- **Audio Ripple Wave Physics**: Sub-bass kicks send physical displacement harmonic ripples across the 3D surface in real time.
- **Scroll Wheel Zoom**: Zoom the 3D camera in and out dynamically.
- **Zero External 3D Libraries**: Pure Canvas 2D projection math running at 60 FPS without Three.js or heavy dependencies.

### 2. ★ Ultra-HD Unicode Braille Matrix ($8\times$ Resolution)
- Uses Unicode Braille patterns (`⠀` to `⣿`, `0x2800`–`0x28FF`) where each character contains an internal **$2 \times 4$ sub-pixel dot matrix**.
- On a typical $120 \times 60$ character grid, the engine samples and dithers **$240 \times 240$ micro-dots in real time**.
- Combined with **Ordered Bayer 4×4 Halftone Dithering**, it preserves intricate lines, textures, and video details impossible with standard ASCII letters.

### 3. 📺 Live Background YouTube Tab Streaming & Music Sync
- Stream any background YouTube video tab directly into the visualizer using Chrome/Edge screen capture.
- Automatically captures the YouTube tab's audio stream and feeds it into the Web Audio FFT analyzer to pulse edges, bloom, chromatic aberration, and 3D wave ripples directly to the video's soundtrack.

### 4. ⚡ Bass-Reactive Chromatic Aberration
- Red and Blue color channels physically split horizontally on heavy kicks and drops, replicating analog cathode-ray CRT deflection in sync with the beat.

### 5. 🌈 Accurate True-Color RGB Sampling
- Samples full 24-bit RGB values from background video streams, rendering each Braille matrix in authentic real-world hues.
- Multiple color palettes: *True Color*, *Vibrant*, *Cyber Neon*, *Matrix Green*, *Amber CRT*, and *Pure Black & White*.

### 6. 🌀 6 Visual Sketches Supported in Both 2D & 3D
- `0` / `Y`: **YouTube Live Stream (8× Braille + True Color + 3D)**
- `1`: **Wave Field (Braille Fluid Dynamics)**
- `2`: **Torus 3D (Braille Geometric Mesh)**
- `3`: **Chladni Plate (Acoustic Sand Resonance)**
- `4`: **Oscilloscope (Braille Laser Beam)**
- `5`: **Vortex (Braille Wormhole)**

---

## ⌨️ Controls & Hotkeys

| Key / Action | Function |
| :--- | :--- |
| **Mouse Left-Click + Drag** | Orbit & Tilt 3D Hologram Camera |
| **Mouse Scroll Wheel** | Zoom In / Out in 3D Mode |
| `[Z]` | Toggle 3D Hologram Depth Field on/off |
| `[R]` | Reset 3D camera to default orientation |
| `[0]` / `[Y]` | YouTube Live Mode / Capture Tab |
| `[1]` – `[5]` | Switch procedural visual sketches |
| `[B]` | Toggle Ultra-HD Braille 8× Dithering |
| `[H]` | Toggle Controls HUD overlay |
| `[F]` | Toggle Fullscreen |

---

## 🚀 Running Locally

Clone the repository and run the built-in multi-threaded local server:
```bash
git clone https://github.com/cbagh0819-ctrl/audio-reactive-ascii.git
cd audio-reactive-ascii
python run.py
```
Or simply double-click and open `index.html` in any modern web browser.

---

## 👨‍💻 Author & Creator

**Chandan Bagh**  
- GitHub: [@cbagh0819-ctrl](https://github.com/cbagh0819-ctrl)  
- Email: [cbagh0819@gmail.com](mailto:cbagh0819@gmail.com)  

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.  
*Copyright (c) 2026 Chandan Bagh. All rights reserved.*
