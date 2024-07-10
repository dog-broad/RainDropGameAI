# 🌧️ Rain Bucket Game 🪣

Welcome to the Rain Bucket Game! This is a simple arcade-style game developed using Python's pygame library. The objective is to catch raindrops using a bucket controlled either by the player or an AI, scoring points for each successful catch within a limited time.

## Features ✨

- Randomly generated raindrops fall from the top of the screen ☔
- Use arrow keys (for Human Control) or an AI heuristic (for AI Control) to move the bucket and catch raindrops 🎮
- Score tracking for each raindrop caught 🌟
- Adjustable game speed to control difficulty ⏩
- Game over condition after a specified duration ⏳

## Requirements 🛠️

- Python 3.x
- pygame library

## Installation 📥

1. Clone the repository:
   
   ```
   git clone <repository-url>
   ```

2. Install pygame:
   
   ```
   pip install pygame
   ```

## How to Play 🕹️

1. **Run the game** by executing `python rain_bucket_game.py`.
   
2. **Select Control Mode**:
   - **Human Control**: Use the left and right arrow keys to move the bucket horizontally.
   - **AI Control**: Let the AI automatically move the bucket towards the nearest raindrop using heuristic rules.

3. **Catch Raindrops**: Position the bucket to catch falling raindrops. Each catch earns you points.

4. **Game Over**: The game ends after a specified duration. You can return to the menu to play again.

---

### Changelog

#### Version 2.8 (Current Version)

- Add sound effects for game events
  - A water drop sound effect is played when a raindrop is caught by the bucket
  - Game Over sound effect is played when the game ends

#### Version 2.7

- The score is reset to 0 when the game ends to ensure a fresh start for the next game. (Bug fix for version 2.6)

#### Version 2.6

- Added bucket colors for human and AI control
- Refactored code to separate Human and AI control modes
- Improved user interface

#### Version 2.5

- Update game duration to 30 seconds in game loop

#### Version 2.4

- Adjust bucket speed for smoother movement

#### Version 2.3 

- The game can be now played with the human and AI control modes.
- Added game over screen with return to menu option.
- Improved look and feel of the start screen.

#### Version 2.2 

- Add control mode selection to start screen
- Refactor code to separate Human and AI control modes

#### Version 2.1

- Enhanced AI control using heuristic rules:
  - Distance Calculation: Calculates the distance between each raindrop and the bucket.
  - Direction Prediction: Predicts the direction of each raindrop's movement (left or right).
  - Optimal Bucket Movement: Moves the bucket towards the predicted landing position of the closest raindrop.

#### Version 2

- Added AI control option for the bucket, automatically moving towards the closest raindrop.
- Improved Start Screen.
- Updated scoring system to reflect AI-controlled catches.

#### Version 1

- Added game over condition after a specified duration (default 30 seconds).
- Enhanced user interface with a start screen featuring a clickable start button.
- Implemented scoring system where players accumulate points for catching raindrops with the bucket.

#### Version 0.2

- Added player-controlled bucket to catch raindrops.
- Implemented collision detection between bucket and raindrops.
- Introduced adjustable game speed to control the falling rate of raindrops.
- Added game over condition after 60 seconds with final score display.

#### Version 0.1

- Implemented basic game structure.
- Added functionality for raindrops to fall from the top of the screen.
- Implemented score tracking for each raindrop that falls off the screen.
