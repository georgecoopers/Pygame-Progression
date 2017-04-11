import random
#Title
TITLE = 'Jumpy'

#Dimensions
WIDTH = 800
HEIGHT = 600
FPS = 60

#Colors
#Primary Colors
RED = (255,0,0)
GREEN = (25,255,0)
BLUE = (0,0,255)

#Secondary Colors
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

#Other Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

RAND_COLOR_ARRAY = [WHITE,YELLOW,MAGENTA,CYAN,RED,BLUE,GREEN]

#Starting platforms
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_LIST = [(0,HEIGHT-40,WIDTH,40,random.choice(RAND_COLOR_ARRAY)),
				(WIDTH/2-50, HEIGHT * 3/4, PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
				(400,200, PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
				(PLATFORM_HEIGHT,300,PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
				(600,50,PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY))]

# Player Properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.5
