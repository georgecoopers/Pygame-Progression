import pygame
# This is the window dimensions
WIDTH, HEIGHT = 800,600

# This is the frames per second
FPS = 60
total_frames = 0

# Colors
WHITE = (255,255,255)

# The screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
gameOver = True

# The pygame window caption
pygame.display.set_caption("Alien Space Invader Attack")

# The pygame clock, allowing me to set the fps of the game
clock = pygame.time.Clock()

# This is the background
backgroundLoad = pygame.image.load("images/background.png")

# The all sprites group
all_sprites = pygame.sprite.Group()

# This is the rocket variables
rocketPath = "images/rocketship.png"
rocketWidth = 75 #px
rocketHeight = 50 #px
rocketX, rocketY = WIDTH / 2, HEIGHT - rocketHeight

# This is the invader variables
invaderPath = "images/invader.png"
invaderWidth = 95 #px
invaderHeight = 50 #px
invaderY = -200
invaderHomeX = 350
invaderHomeY = 10

# This is the bullet variables
bulletPath = "images/bullet.png"
bulletWidth,bulletHeight = 3, 62 


