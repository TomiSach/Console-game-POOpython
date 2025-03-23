# Dungeon Travel Console Game

Welcome to the Dungeon Travel Console Game! This is a simple console-based game implemented in Python using Object-Oriented Programming (OOP) principles.

## Overview

In this game, you play as a hero who ventures into a dungeon and encounters various villains. You can choose to attack the villains or run away. The game continues until you defeat all the villains or your health drops to zero.

## How to Play

1. Run the `main.py` script.
2. Enter your name when prompted.
3. Follow the instructions to attack or run from the villains.
4. Gain experience and level up as you defeat villains.
5. Continue the adventure until all villains are defeated or your health drops to zero.

## Code Structure

### `main.py`

This is the main script that runs the game. It initializes the player and the list of villains, and contains the game loop where the player encounters and battles villains.

### `clases/player.py`

This file contains the `Player` class, which represents the hero. The class includes methods for attacking, receiving damage, and gaining experience.

### `clases/villain.py`

This file contains the `Villain` class, which represents the enemies the player encounters. The class includes methods for attacking and receiving damage.

## Classes

### `Player`

- **Attributes**:
  - `name`: The name of the player.
  - `health`: The health of the player, initialized to 100.
  - `level`: The level of the player, initialized to 1.
  - `experience`: The experience points of the player, initialized to 0.

- **Methods**:
  - `attack()`: Returns a random attack value based on the player's level.
  - `receive_damage(damage)`: Reduces the player's health by the damage amount and prints a message if the player's health drops to zero.
  - `gain_experience(experience)`: Increases the player's experience points and levels up if the experience reaches 100.

### `Villain`

- **Attributes**:
  - `name`: The name of the villain.
  - `health`: The health of the villain.
  - `damage`: The damage the villain can inflict.

- **Methods**:
  - `attack()`: Returns a random attack value.
  - `receive_damage(damage)`: Reduces the villain's health by the damage amount and prints a message if the villain's health drops to zero.

## Game Flow

1. The player is prompted to enter their name.
2. The game initializes the player and a list of villains.
3. The player encounters random villains and chooses to attack or run.
4. The player gains experience and levels up by defeating villains.
5. The game ends when all villains are defeated or the player's health drops to zero.

## Conclusion

Enjoy your adventure in the dungeon! Defeat all the villains and become the ultimate hero!
