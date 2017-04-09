import pygame, random
# The settings are all the global variables that i need
from settings import *

class Rocket(pygame.sprite.Sprite):
    # This is the rocket group for the rocket sprite to be stored in
    rocketGroup = pygame.sprite.Group()
    def __init__(self,x,y,width,height,imageString):

        # This intitializes the pygame sprite init function
        pygame.sprite.Sprite.__init__(self)

        # This adds the rocket to the 'rocketGroup'
        Rocket.rocketGroup.add(self)

        # This loads the spaceship.png to the variable 'image'
        self.image = pygame.image.load(imageString)

        # This gets the dimensions of the spaceship image 
        self.rect = self.image.get_rect()

        # This is the x and y coordinates of the spaceship
        self.rect.centerx = x 
        self.rect.centery = y
        
        self.rect.width = width
        self.rect.height = height

        # This is the x velocity of the spaceship
        self.velX = 0

    def update(self):

        # This is the key press variable
        keys = pygame.key.get_pressed()

        # This is the movement of the spaceship
        self.rect.x += self.velX

        # This is the event handling of the spaceship
        if keys[pygame.K_d]:
            self.velX = 4
        elif keys[pygame.K_a]:
            self.velX = -4
        else:
            self.velX = 0

        # This prevents the spaceship from moving off the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

    def Shoot(self):
        # If the player shoots the bullet object is created and add to the all_sprites group
        bullet = Bullet(self.rect.centerx, self.rect.top, bulletWidth, bulletHeight, bulletPath)
        all_sprites.add(bullet)
            
class Bullet(pygame.sprite.Sprite):
    # This is the bullet group
    bulletGroup = pygame.sprite.Group()
    def __init__(self,x,y,width,height,imageString):

        # This intitializes the pygame sprite init function
        pygame.sprite.Sprite.__init__(self)

        # Adds the bullet to the bullet group
        Bullet.bulletGroup.add(self)

        # This loads the image path to the self.image variable
        self.image = pygame.image.load(imageString)

        # This gets the dimensions of the image
        self.rect = self.image.get_rect()

        # This sets the x and y cneter coords of the bullet
        self.rect.centerx = x
        self.rect.centery = y

        # This sets the width and height of the bullet
        self.rect.width = width
        self.rect.height = height

        # This is the y velocity of the bullet
        self.velY = 20
        
    def update(self):

        # This is the movement of the bullet 
        self.rect.centery -= self.velY

        # If the bullet goes off the screen it is kill, (removed from any groups)
        if self.rect.bottom < 0:
            self.kill()



class Invader(pygame.sprite.Sprite):
    # This is the invaders group
    invaderGroup = pygame.sprite.Group()
    
    def __init__(self,x,y,width,height,imageString):
        # This intitializes the pygame sprite init function
        pygame.sprite.Sprite.__init__(self)

        # This adds the invader to the 'invaderGroup'
        Invader.invaderGroup.add(self)

        # This loads the invader image to the 'image' variable
        self.image = pygame.image.load(imageString)

        # This gets the dimensions of the invader.png image
        self.rect = self.image.get_rect()

        # This sets the coordinates of the invader
        self.rect.x = x
        self.rect.y = y

        # This sets the width and height of the invader 
        self.rect.width = width
        self.rect.height = height

        # This sets random y velocity of the invader
        self.velY = random.randint(1,2)
        
    def update(self):
        # This adds the y velocity to the invaders y velocity to cause it to move
        self.rect.y += self.velY

        if self.rect.y < -50:
            spawn()

        # This terminates the invader when it goes past the screen
        if self.rect.y > HEIGHT:
            spawn()
            self.kill()

    # This static method is called to move all the Invaders
    @staticmethod
    def motion():
        for invaders in Invader.invaderGroup:
            invaders.update()

# This is called when ever a Invader dies or leaves the screen
def spawn():
    if len(Invader.invaderGroup) < 20:
        invaderX = random.randint(0,700)
        invader = Invader(invaderX,invaderY,invaderWidth,invaderHeight,invaderPath)
        all_sprites.add(invader)

# This function is used anytime i want to write text to the screen   
def display_text(message,x,y,size,color):
    font = pygame.font.SysFont("Comic Sans Ms", size)
    text = font.render(message,False,color)
    screen.blit(text,(x,y))

# This function shows the game over and start screen                
def show_go_screen(highscore):
    gameStart = False
    while not gameStart:
        screen.blit(backgroundLoad, (0,0))
        display_text("Welcome to Space Invader Attack!",WIDTH/3-100,HEIGHT/4,30,WHITE)
        display_text("A and D to move left and right and SPACE to shoot",WIDTH/3-20,HEIGHT/3,15,WHITE)
        display_text("Press any button to continue...",WIDTH/3+50,HEIGHT*2/3,15,WHITE)
        display_text(("Highscore:"+highscore),WIDTH/3+50,HEIGHT/1.75,15,WHITE)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                gameStart = True
      
# This function detects any collisions
def collisions():
    for invaders in Invader.invaderGroup:
        collide = pygame.sprite.spritecollide(invaders,Rocket.rocketGroup,True)

    hit = pygame.sprite.groupcollide(Bullet.bulletGroup,Invader.invaderGroup,True,True)
    for hits in hit:
        spawn()
    if hit:
        return 1

