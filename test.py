import pytest
from snakegame import Snake, Food, check_collision, change_dir

# Constants for the game dimensions
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 30

@pytest.fixture
def snake():
    # Initialize the snake
    return Snake()

@pytest.fixture
def food():
    # Initialize the food
    return Food()

def test_snake_initialization(snake):
    # Test if snake is initialized with correct number of body parts
    assert len(snake.coordinates) == 3
    assert len(snake.squares) == 3

def test_food_initialization(food):
    # Test if food is initialized within game boundaries
    assert 0 <= food.coordinates[0] < GAME_WIDTH
    assert 0 <= food.coordinates[1] < GAME_HEIGHT

def test_check_collision_with_walls(snake):
    # Test collision with walls
    snake.coordinates = [[-10, 0]]  # Simulate the snake going out of bounds (left wall)
    assert check_collision(snake) == True

    snake.coordinates = [[GAME_WIDTH, 0]]  # Simulate the snake going out of bounds (right wall)
    assert check_collision(snake) == True

    snake.coordinates = [[0, -10]]  # Simulate the snake going out of bounds (top wall)
    assert check_collision(snake) == True

    snake.coordinates = [[0, GAME_HEIGHT]]  # Simulate the snake going out of bounds (bottom wall)
    assert check_collision(snake) == True

def test_check_collision_with_self(snake):
    # Test collision with self
    snake.coordinates = [[100, 100], [100, 130], [100, 160], [100, 100]]  # Simulate the snake head colliding with body
    assert check_collision(snake) == True

    snake.coordinates = [[100, 100], [130, 100], [160, 100], [190, 100]]  # No collision with self
    assert check_collision(snake) == False

def test_change_direction():
    global direction
    direction = 'left'
    change_dir('right')  # Snake shouldn't be able to go in the opposite direction
    assert direction == 'left'

    change_dir('up')  # Valid direction change
    assert direction == 'up'

    change_dir('down')  # Snake shouldn't be able to go in the opposite direction
    assert direction == 'up'

    change_dir('left')  # Valid direction change
    assert direction == 'left'
