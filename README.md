# 🌧️ Rain Bucket Game - Human vs. AI 🪣

Welcome to the Rain Bucket Game! This is an arcade-style game developed using Python's pygame library, now featuring both Human and AI modes. The objective remains the same: catch raindrops using a bucket and score points within a limited time.

## Features ✨

- Randomly generated raindrops fall from the top of the screen ☔
- **Human Control Mode**: Use arrow keys to move your bucket and catch raindrops 🎮
- **AI Control Mode**: Let the AI move the bucket using heuristic rules to catch raindrops automatically 🤖
- Separate scoring for Human and AI players, displayed during and after the game 🌟
- Adjustable game speed to control difficulty ⏩
- Game over condition after a specified duration ⏳
- Sound effects for catching raindrops and game over events 🔊

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
   
2. **Start the Game**:
   - Click on **Start Game** on the main menu to begin.
   
3. **Select Control Mode**:
   - **Human Control**: Use the left and right arrow keys to move the human bucket.
   - **AI Control**: Watch as the AI automatically moves its bucket to catch raindrops based on heuristic rules.

4. **Catch Raindrops**: Position your bucket(s) to catch falling raindrops. Each catch earns points for the respective player (Human or AI).

5. **Game Over**: The game ends after 30 seconds. You can return to the menu to play again.

---

### Changelog

#### Version 2.9 (Current Version)

- Users can now play against an AI
- Game Over screen now displays final score and game result

#### Version 2.8 

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
