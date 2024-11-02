# Number Guessing Game

## Overview

The **Number Guessing Game** is a desktop application built with Python's Tkinter library. This game challenges users to guess a randomly generated number within a defined range, giving feedback on each attempt. The game provides an interactive and enjoyable way to practice number comparison logic, user input handling, and basic GUI design.

## Features

- **Set Number Range**: Allows users to define the maximum number for the guessing range, adding flexibility to the gameplay.
- **Random Number Generation**: A new target number is generated each game to ensure varied and unpredictable gameplay.
- **Feedback Mechanism**: Provides hints (e.g., “Too high!” or “Too low!”) based on the user’s guess, helping guide them towards the correct number.
- **Attempts Counter**: Tracks and displays the number of attempts made for each game.
- **Restart Game**: A "New Game" button is available to quickly restart the game with a fresh target number.

## What I Learned

This project helped reinforce key concepts and techniques:
- **GUI Development with Tkinter**: Developed a structured, interactive graphical interface using Tkinter widgets such as Labels, Entry fields, and Buttons.
- **Random Number Generation**: Used Python’s `random` module to generate a random number within a specified range, ensuring unpredictable gameplay.
- **Input Validation and Error Handling**: Added checks for valid integer inputs and provided user feedback when inputs were invalid or out of range.
- **Dynamic Updates with Tkinter Variables**: Used `StringVar` to dynamically update text and track changes in the GUI for real-time feedback on user interactions.
- **Game Logic**: Built a simple but effective guessing game loop that provides guidance to players and encourages them to guess until they find the target number.

## Installation

1. **Requirements**:
   - Python 3.x
   - Tkinter (usually pre-installed with Python)

2. **Installation**:
   - Clone this repository:  
     ```bash
     git clone <repository-url>
     ```
   - Run the `number_guessing_game.py` script:
     ```bash
     python number_guessing_game.py
     ```

## Usage

1. **Setting the Range**: Enter a maximum number and click "Set" to define the range for the random number (default is 100).
2. **Guessing**: Enter a guess in the input field and press **Enter** or click the **Guess** button. 
3. **Hints**: The app will tell you if your guess is too high or too low, allowing you to adjust accordingly.
4. **New Game**: Click **New Game** to restart with a fresh target number.

## Example Gameplay

- **Input**: User sets the range to 50 and guesses 30.
- **Output**: Feedback displays "Too low! Try a higher number."
- **Success**: When the user guesses correctly, they see a congratulatory message with the number of attempts used.

## Future Enhancements

- Add a difficulty setting (e.g., Easy, Medium, Hard) that adjusts the range automatically.
- Implement a leaderboard to track high scores (least attempts to guess correctly).
- Add sound effects and animations for an enhanced user experience.
