*work in progress*

# Vampire's Escape: A Game of Garlic and Survival

Welcome to **Vampire's Escape**! A thrilling, fast-paced game developed using **Pygame**. In this game, you play as a vampire trying to escape an ever-approaching **garlic**, which he is severely allergic to. The game features pseudo-3D gameplay inspired by classics like **DOOM**, where you must navigate a maze, avoid the garlic, and survive the chase.

## Table of Contents

- [About the Game](#about-the-game)
- [Game Features](#game-features)
- [Installation Instructions](#installation-instructions)
- [Gameplay Mechanics](#gameplay-mechanics)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About the Game

Vampire's Escape puts you in the shoes of a vampire with a singular goal: **Run from the garlic**. The game is set in a randomly generated maze in each level, with the garlic chasing you relentlessly. As the garlic moves closer, your health decreases, and if it gets too close, it's game over. The vampire cannot fight the garlic but has the ability to **hide** in certain spots within the maze to catch a breath and regroup. 

Inspired by classic **DOOM** but with a unique twist, **Vampire's Escape** is designed to test your reflexes, speed, and decision-making skills as you navigate through challenging mazes.

---

## Game Features

- **Pseudo-3D Environment**: The game uses a 3D perspective where the vampire moves through a maze, making it feel like a real 3D world despite being rendered using simple 2D graphics.
- **Randomly Generated Mazes**: Each level presents a unique challenge with randomly generated mazes, ensuring that no two playthroughs are the same.
- **Garlic Chase Mechanism**: The main antagonist, a jpeg of garlic, chases you. The closer it gets, the more your health depletes. 
- **Health Management**: You have limited health, and hiding from the garlic helps to regain it. The longer you run, the more chances you get to survive.
- **Hiding Spots**: The maze contains secret spots where you can hide from the garlic to avoid being caught.
- **Multiple Levels**: As you progress, the mazes become more complex, and the garlic gets more aggressive in its chase.
- **Simple Controls**: Focus on navigating the maze without complex combat systems. Run, hide, and survive!

---

## Installation Instructions

To install and run **Vampire's Escape**, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nupjan/Scared_Dracula.git
   ```
   
2. **Navigate into the project folder**:
   ```bash
   cd Scared_Dracula
   ```
   
3. **Install required dependencies**:
   Ensure that you have **Python** and **Pygame** installed.
   ```bash
   pip install pygame
   ```

4. **Run the game**:
   ```bash
   python main.py
   ```

---

## Gameplay Mechanics

### Controls:
- **Arrow Keys**: Move the vampire through the maze.
- **Spacebar**: Hide in hiding spots within the maze to temporarily evade the garlic.
- **ESC**: Pause the game.

### Objective:
- **Main Goal**: Survive the chase by running from the garlic and reaching the finish line of the maze.
- **Hiding Mechanism**: Use hiding spots to regain health and escape the garlic's wrath temporarily.
- **Health Management**: Keep an eye on your health bar; running away from garlic is your only defense!

---

## Project Structure

The project follows a clean and simple structure to ensure maintainability and scalability:

```
Scared_Dracula/
│
├── Images/              # Contains images, sounds, and other media files
│   ├── garlic.jpg       # Image of the garlic
│   ├── Dracula.jpg      # Image of the vampire character
│   ├── background.jpg   # Maze background
│
├── main.py              # Main game file, entry point of the game
├── generate_maze.py    # Logic for generating random mazes
├── game_logic.py        # Contains the core game mechanics
├── utils.py             # Utility functions for handling various tasks
│
└── README.md            # This file
```

---

## Technologies Used

- **Python**: The programming language used for game development.
- **Pygame**: The library used to create the game, handle graphics, and manage game loops.
- **Random**: Used to generate unique mazes for every level.

---

## Contributing

We welcome contributions to make **Vampire's Escape** even better! If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---



## Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [https://github.com/Nupjan](https://github.com/yourusername)


---

