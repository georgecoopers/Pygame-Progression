# Pygame Space Invader Attack
import pygame
import random
from classes import *
from settings import *

# Initialize Pygame and Pygame Mixer
pygame.init()
pygame.mixer.init()

# Sets the score 
score = 0

highscoreFile = open("extra_files/highscore.txt","r+")
read = highscoreFile.readlines()
# Game Loop
gameRunning = True
while gameRunning:

    # This starts game over screen
    if gameOver:

        # This if statement below checks if the highscore has been beaten.
        if int(read[0]) < int(score):
            highscoreFile.seek(0)
            highscoreFile.truncate()
            highscoreFile.write(str(score))
            highscoreFile.close()
            highscoreFile = open("extra_files/highscore.txt","r+")
            read = highscoreFile.readlines()

            
            
        # This calls the game over function
        show_go_screen(str(read[0]))

        # This resets the score
        score = 0

        # When the user goes to home screen the rocket and invaders are reset

        # Rocket variables
        rocket = Rocket(rocketX,rocketY,rocketWidth,rocketHeight,rocketPath)
        all_sprites.add(rocket)

        # The invaders get given a random X coordinate
        invaderX = random.randint(0,700)

        # This is the invader object
        invader = Invader(invaderX,invaderY,invaderWidth,invaderHeight,invaderPath)

        # The invader is added to the all_sprites group
        all_sprites.add(invader)

        #This breaks the 'gameOver' screen loop
        gameOver = False
    
    #This displays the background image
    screen.blit(backgroundLoad, (0,0))
    
    clock.tick(FPS)
    # Process input (events)
    

    # This is an event handling loop    
    for event in pygame.event.get():

        # This quits the game if the user clicked on the cross
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # This shoots if the user clicked the space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rocket.Shoot()
                
    
    # Update

    # This updates all the sprites
    all_sprites.update()

    # This updates the motion of the aliens
    Invader.motion()

    # This detects whether the bullet has collided with the aliens
    if collisions() == 1:
        score += 1

    # This detects if the rocket has been killed, if it has then everything gets reset
    if len(Rocket.rocketGroup) == 0:
        for everything in all_sprites:
            everything.kill()
        gameOver = True

    # Draw / render
    display_text(("Points:"+str(score)),0,0,30,WHITE)
    # This blits the bacground image

    # This draws all the sprites to the screen
    all_sprites.draw(screen)

    # This updates the screen entirely
    pygame.display.flip()

#This quits pygame
pygame.quit()

#This quits python
quit()
                          
