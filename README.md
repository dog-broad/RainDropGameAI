# Rain Bucket Game

This is a simple pygame-based game where raindrops fall from the top of the screen, and the player controls a bucket to catch them, scoring points for each successful catch within a limited time.

## Features

- Randomly generated raindrops that fall from the top of the screen.
- Bucket controlled by arrow keys to catch raindrops.
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

---

### Changelog

#### Version 1 (Current Version)

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
