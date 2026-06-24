# Python Final Project
98mathz-a11y (well, tbh, he only wrote 1 line in the ENTIRE project), Wal0fsky working on a small project using the python library pygame

A small top-down Pygame arcade game built in Python. The player controls a UFO-like ship, moves around the screen, shoots projectiles, and avoids enemies that spawn around the edges and move toward the player.

## Features

- Player movement with forward and backward thrust
- Rotation with left and right turning controls
- Projectile shooting with a cooldown
- Enemies that spawn randomly at screen edges
- Enemy movement toward the player
- Collision detection between enemies, the player, and projectiles
- Score tracking when enemies are destroyed

## Controls

- `W` - move forward
- `S` - move backward
- `A` - rotate left
- `D` - rotate right
- `Space` - shoot
- Window close button - quit the game

## Requirements

- Python 3
- `pygame`
- `matplotlib`

Install the dependencies with:

```bash
pip install pygame matplotlib
```

## How To Run

Make sure the image assets are in the project folder, then run:

```bash
python game.py
```

If your system uses a virtual environment, activate it first and run the same command inside it.

## Project Structure

- `game.py` - main game loop, input handling, spawning, drawing, and score logic
- `logic.py` - shared game object classes for the player, projectile, and enemy
- `player.png` - player sprite asset
- `enemy.png` - enemy sprite asset

## Gameplay Notes

- Enemies spawn at random screen edges and move toward the player.
- Projectiles travel in the direction the player is facing.
- A projectile and enemy are removed when they collide.
- The game ends when an enemy touches the player.

## Implementation Notes

- Movement and rotation are handled through a shared base class.
- The player and enemy use rotated hitbox points for collision checks.
- Collision detection currently uses `matplotlib.path.Path` for polygon intersection.

## Possible Improvements

- Add a start menu or restart screen
- Add sound effects and music
- Replace the current collision system with a lighter approach
- Add health instead of instant game over
- Improve projectile spawning so shots originate from the ship's nose

## Credits

Created as a Python/Pygame final project.

## AI usage

The core ideas and implementation of this project are our own. We developed the concept, researched functions and libraries online (mainly through the Pygame documentation, Google AI Mode, and Stack Overflow), and implemented the solutions ourselves. AI was used only to a limited extent, primarily for debugging, exploring possible approaches to new problems, and answering general questions related to Python logic and programming concepts. All code in this project was written by us.
