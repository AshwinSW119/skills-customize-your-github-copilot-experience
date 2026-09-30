
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, and user input to let a player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the game logic that chooses a word from a list and prepares the hidden word display for the player.

#### Requirements
Completed program should:

- Select a random word from a predefined list of words
- Show the hidden word as underscores, such as `_ _ _ _ _`
- Allow the player to enter one letter at a time
- Update the visible word when the guess is correct
- Keep track of guessed letters to avoid repeating guesses

### 🛠️ Game Loop and Win/Lose Logic

#### Description
Add the gameplay loop that checks guesses, tracks mistakes, and ends the game when the player wins or loses.

#### Requirements
Completed program should:

- Reduce the remaining attempts when a guess is incorrect
- Display the current hangman state or remaining attempts clearly
- Check whether the player has guessed the full word
- End the game with a win message when the word is completed
- End the game with a lose message when attempts are exhausted
