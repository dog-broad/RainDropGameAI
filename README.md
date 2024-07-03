# Rain Bucket Game

This is a simple pygame-based game where raindrops fall from the top of the screen, and the player controls a bucket to catch them, scoring points for each successful catch within a limited time.

## Features

- Randomly generated raindrops that fall from the top of the screen.
- Bucket controlled by arrow keys to catch raindrops.
- AI-controlled option to automatically move the bucket towards the nearest raindrop using heuristic rules.
- Score tracking for each raindrop caught.
- Adjustable game speed to control the difficulty.
- Game over condition after a specified duration.

## Requirements

- Python 3.x
- pygame library

## Installation

1. Clone the repository:
   
   ```
   git clone <repository-url>
   ```

2. Install pygame:
   
   ```
   pip install pygame
   ```

## How to Play

- Run the game by executing `python rain_bucket_game.py`.
- Use the left and right arrow keys to move the bucket horizontally to catch raindrops within the given time limit.
- Alternatively, enable AI mode to automatically control the bucket using heuristic rules.

---

### Changelog

#### Version 2.5 (Current Version)

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
