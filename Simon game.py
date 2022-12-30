import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 708)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Simon's Flappy Bird")

# Load the images
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.png")
heart_image = pygame.image.load("heart.png")

# Set the bird's starting position
bird_x = 50
bird_y = 350

# Set the bird's movement speed
bird_speed = 0

# Set the gravity
gravity = 0.25

# Set the pipe gap size
pipe_gap_size = 100

# Set the distance between pipes
pipe_distance = 300

# Set the pipe speed
pipe_speed = -2

# Set the pipe width
pipe_width = 80

# Set the pipe height
pipe_height = 708

# Set the pipe positions
pipe_1_x = 400
pipe_1_y = 0

pipe_2_x = 700
pipe_2_y = 0

# Set the heart position
heart_x = 600
heart_y = random.randint(0, 434)

# Set the game over flag
game_over = False

# Set the font
font = pygame.font.Font(None, 36)
