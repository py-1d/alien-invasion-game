# 👾 Alien Invasion Arcade Game

A 2D retro-style arcade game built in Python using the Pygame library. The player controls a spaceship, fires lasers, and fends off waves of invading aliens.

## 🚀 Features
- Object-oriented game architecture (Player, Alien, Bullets, Game state)
- Real-time collision detection using `pygame.sprite.Group`
- Sprite animations, sound effects, and level-based difficulty scaling
- Reset and round progression with HUD display for score, lives, and rounds

## 🎮 Controls
- ⬅️ / ➡️ : Move the spaceship
- SPACE : Fire a bullet
- ESC : Quit the game

## 🧠 Technologies Used
- Python 3.x
- Pygame

## 📦 Installation
```bash
pip install pygame
```

## 🏁 Run the Game
```bash
python space_invaders_V2.py
```

## 📁 Folder Structure
- `space_invaders_V2.py` : Main game loop and logic
- `PlayerClass.py` : Player and bullet logic
- `AlienClass.py` : Alien movement, bullet logic, and behaviors
- `assets/` : Folder expected to contain images and sound files (not included)

## 📄 License
MIT License
