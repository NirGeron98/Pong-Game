
# Pong Game

This project is a classic Pong game, built as part of the "100 Days of Code: The Complete Python Pro Bootcamp" on Udemy. The game was developed using Python's `turtle` module, allowing two players to compete by controlling paddles and attempting to hit a ball back and forth across the screen.

## Project Structure

The project consists of the following Python files:

- **main.py**: The main file that initializes the game, sets up the screen, and contains the game loop.
- **paddle.py**: Defines the `Paddle` class, which controls the movement of the paddles on the screen.
- **ball.py**: Defines the `Ball` class, responsible for moving the ball and detecting collisions with paddles and walls.
- **scoreboard.py**: Defines the `Scoreboard` class, which keeps track of and displays the score for both players.

## How to Play

- Player 1 controls the left paddle using the "W" and "S" keys to move up and down.
- Player 2 controls the right paddle using the "Up" and "Down" arrow keys.
- The objective is to hit the ball with your paddle and try to get it past your opponent's paddle. Each time the ball passes an opponent's paddle, you score a point.
- The game continues indefinitely, with the score being tracked on the screen.

## How to Run the Game

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pong-game.git
   cd pong-game
   ```

2. **Run the game:**

   You can run the game by executing the `main.py` file:

   ```bash
   python main.py
   ```

3. **Play the game:**

   After running the game, a window will appear where two players can start playing by controlling their respective paddles.

## Key Components

### Paddle

The `Paddle` class is responsible for the paddles' movement. Each paddle can move up or down within the screen boundaries. The class also handles the key press and release events for smooth paddle movement.

### Ball

The `Ball` class manages the ball's movement across the screen. It includes methods for bouncing the ball off the walls and paddles, and resetting its position when it passes a paddle.

### Scoreboard

The `Scoreboard` class tracks and displays the score for both players. The score is updated each time the ball passes a player's paddle.

## Future Enhancements

- Add a feature to track high scores.
- Implement a difficulty setting to adjust the ball speed.
- Improve the graphics and user interface.
