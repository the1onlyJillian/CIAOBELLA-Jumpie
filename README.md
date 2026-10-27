# 🎀 Ciaobella Jumpie

*Skill issue? Ciaobella could never. 💅🎀*

**Ciaobella Jumpie** is a vertical jumping game built with Python and Pygame, starring Ciaobella! Help her jump across platforms, climb higher, and survive as the game gets harder.

Sounds easy? Wait until the platforms start moving. 👀

## ✨ Features

- 🦘 **Vertical Jumping** — jump across platforms and keep climbing.
- 📈 **Score System** — earn points as the camera scrolls upward.
- 🪵 **Standard Platforms** — land on regular platforms to continue climbing.
- 🔵 **Moving Platforms** — blue platforms appear at 1,000 points and move horizontally.
- ❤️ **Breakable Platforms** — red platforms appear at 2,000 points and disappear after being landed on.
- 🌍 **Screen Wrapping** — move past one horizontal edge to appear on the opposite side.
- 🎚️ **Progressive Difficulty** — new platform challenges appear as your score increases.
- 💀 **Chaotic Game Over** — fall too far and get greeted with *"SKILL ISSUE DEK >_<"*.
- 🔄 **Quick Restart** — press `SPACE` to try again.

## 🎮 How to Play

| Key | Action |
|---|---|
| `←` or `A` | Move Ciaobella left |
| `→` or `D` | Move Ciaobella right |
| `SPACE` | Restart after game over |

### Difficulty Levels

| Score | Level | Platform Types |
|---|---|---|
| Below 1,000 | 🌱 Easy | Standard |
| 1,000–1,999 | ⚡ Medium | Standard and moving |
| 2,000 and above | 🔥 Hardcore | Standard, moving, and breakable |

**The goal:** Help Ciaobella climb as high as possible and beat your highest score!

## 🛠️ Built With

- **Python** — game logic, movement, scoring, and difficulty progression.
- **Pygame** — game window, keyboard input, sprites, collision detection, rendering, and game loop.
- **Random Module** — randomized platform positions, movement directions, and platform type selection.

## 🚀 Getting Started

### Prerequisites

- Python 3
- Pygame
- The image assets `sky.png` and `orang.png`

### Installation

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project folder:

   ```bash
   cd ciaobella-jumpie
   ```

3. Install Pygame:

   ```bash
   python -m pip install pygame
   ```

4. Make sure `sky.png`, `orang.png`, and your Python script are in the same project directory.

5. Run the game:

   ```bash
   python main.py
   ```

   Replace `main.py` with your actual Python filename if it is different.

## 📁 Project Structure

```text
ciaobella-jumpie/
├── main.py
├── sky.png
├── orang.png
└── README.md
```

*Example structure — adjust the filenames and folders to match your repository.*

## 🧠 What I Learned

- Building a game loop and managing FPS.
- Handling keyboard input and player movement.
- Applying gravity and jump velocity.
- Detecting collisions between the player and platforms.
- Creating a scrolling camera effect.
- Managing sprite groups and generating platforms dynamically.
- Implementing score-based difficulty progression.
- Handling game-over and restart states.

## 💡 Future Improvements

- Add a high-score system.
- Introduce more platform types and obstacles.
- Add sound effects and background music.
- Improve Ciaobella's animations.
- Add more chaotic game-over messages.

## 🎀 One Last Thing

Fall down? Skill issue, dek.

Get back up, press `SPACE`, and let Ciaobella slay again. :p

---

*Made with Python, Pygame, and a little bit of chaos.* 💗
