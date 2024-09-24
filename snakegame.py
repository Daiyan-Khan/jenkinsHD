# snake_game.py
# Snake Game
# This code implements a classic Snake game using tkinter in Python. The player controls a snake that moves around the game board,
# eating food and growing in length. The objective is to eat as much food as possible without colliding with the walls or the snake's own body.

from tkinter import *
import random

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
GAME_SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = 'light green'
FOOD_COLOR = 'red'
BG_COLOR = 'black'

# Snake class
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize snake body coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Create snake body squares
        for x, y in self.coordinates:
            s = can.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(s)

# Food class
class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Create food oval
        can.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

# Move snake in the next turn
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    # Update snake coordinates and squares
    snake.coordinates.insert(0, (x, y))
    s = can.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, s)

    # Check if snake has eaten the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        score_label.config(text="Score: {}".format(score))
        can.delete('food')
        food = Food()
    else:
        # Remove the last segment of the snake
        del snake.coordinates[-1]
        can.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collision with walls or self
    if check_collision(snake):
        game_over()
    else:
        w.after(GAME_SPEED, next_turn, snake, food)

# Change snake direction
def change_dir(new_dir):
    global direction

    # Ensure the snake cannot turn back on itself
    if new_dir == 'left' and direction != 'right':
        direction = new_dir
    elif new_dir == 'right' and direction != 'left':
        direction = new_dir
    elif new_dir == 'up' and direction != 'down':
        direction = new_dir
    elif new_dir == 'down' and direction != 'up':
        direction = new_dir

# Check for collision with walls or self
def check_collision(snake):
    x, y = snake.coordinates[0]

    # Check collision with walls
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        print("Game over - collision with walls")
        return True

    # Check collision with self
    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            print("Game over - collision with self")
            return True

    return False

# Game over function
def game_over():
    can.delete(ALL)
    can.create_text(can.winfo_width() / 2, can.winfo_height() / 2,
                    font=('Arial', 30), text="GAME OVER", fill='red', tag='over')

# Create the main window
w = Tk()
w.title('Snake Game')
w.resizable(False, False)

# Initialize score
score = 0
direction = 'down'

# Create score label
score_label = Label(w, text="Score: {}".format(score), font=('Helvetica', 40))
score_label.pack()

# Create game canvas
can = Canvas(w, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
can.pack()

w.update()
win_width = w.winfo_width()
win_height = w.winfo_height()
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))
w.geometry(f'{win_width}x{win_height}+{x}+{y}')

# Initialize snake and food
snake = Snake()
food = Food()

# Start the game
next_turn(snake, food)

# Bind arrow keys to change snake direction
w.bind('<Left>', lambda event: change_dir('left'))
w.bind('<Right>', lambda event: change_dir('right'))
w.bind('<Up>', lambda event: change_dir('up'))
w.bind('<Down>', lambda event: change_dir('down'))

w.mainloop()
