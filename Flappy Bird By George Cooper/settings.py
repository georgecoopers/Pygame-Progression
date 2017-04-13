import random
import pygame as pg
# Settings
WIDTH, HEIGHT = 800, 600
TITLE = "Flappy Bird"
FPS = 60

# Colors
# Primary Colors
RED = (255,0,0)
GREEN = (25,255,0)
BLUE = (0,0,255)

# Secondary Colors
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# Other Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Player Properties
PLAYER_GRAV = 0.52
BIRD_PATH = "images/flappybird.png"

#Tube Properties
TUBE_COLOR = (50,255,0)
TUBE_X = 800
TUBE_Y = 0
TUBE_WIDTH = 100

# Background
Background = pg.image.load("images/skybackground.png")
SAND = (255,255,100)
