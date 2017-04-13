import pygame as pg
import random
from settings import *
from sprites import *
class Game:
    def __init__(self):
        #Initialize Pygame and Create Window
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        
    def new(self):
        # Start a New Game

        # Groups
        self.all_sprites = pg.sprite.Group()
        self.groundGroup = pg.sprite.Group()
        self.tubes = pg.sprite.Group()

        # Player Object
        self.player = Player(BIRD_PATH)
        self.all_sprites.add(self.player)
        self.PLAYER_SCORE = 0

        # Ground Object
        self.ground = Ground(0,550,800,50)
        self.groundGroup.add(self.ground)
        self.all_sprites.add(self.ground)

        # Tube object and properties
        TUBE_HEIGHT = random.randint(100,300)
        TUBE_GAP = random.randint(150,250)

        self.tubeTop = Tube(TUBE_X,TUBE_Y,TUBE_WIDTH,TUBE_HEIGHT,TUBE_COLOR)
        self.tubeBottom = Tube(TUBE_X,TUBE_HEIGHT+TUBE_GAP,TUBE_WIDTH,HEIGHT-50-(TUBE_HEIGHT+TUBE_GAP),TUBE_COLOR)
        self.tubes.add(self.tubeBottom)
        self.tubes.add(self.tubeTop)
        self.all_sprites.add(self.tubeTop)
        self.all_sprites.add(self.tubeBottom)
        self.highscoreFile = open("extra_files/highscore.txt","r+")
        self.read = self.highscoreFile.readlines()




    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update

        #This is the all sprites group
        self.all_sprites.update()
     
     	# This spawns a new random set of tubes when the tubes reach 200px
        if self.tubeBottom.rect.x == 300:
        	self.PLAYER_SCORE += 1
        	TUBE_HEIGHT = random.randint(100,300)
        	TUBE_GAP = random.randint(150,250)
        	self.tubeTop = Tube(TUBE_X,TUBE_Y,TUBE_WIDTH,TUBE_HEIGHT,TUBE_COLOR)
        	self.tubeBottom = Tube(TUBE_X,TUBE_HEIGHT+TUBE_GAP,TUBE_WIDTH,HEIGHT-50-(TUBE_HEIGHT+TUBE_GAP),TUBE_COLOR)
        	self.tubes.add(self.tubeBottom)
        	self.tubes.add(self.tubeTop)
        	self.all_sprites.add(self.tubeTop)
        	self.all_sprites.add(self.tubeBottom)
        if int(self.read[0]) < int(self.PLAYER_SCORE):
        	self.highscoreFile.seek(0)
        	self.highscoreFile.truncate()
        	self.highscoreFile.write(str(self.PLAYER_SCORE))
        	self.highscoreFile.close()
        	self.highscoreFile = open("extra_files/highscore.txt","r+")
        	self.read = self.highscoreFile.readlines()



    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.vel.y = -10

        groundCollide = pg.sprite.spritecollide(self.player,self.groundGroup,False)

        # This detects if the player has collided with the ground
        if groundCollide:
        	self.playing = False

        # This detects if the player has collided with the tube
        tubeCollide = pg.sprite.spritecollide(self.player,self.tubes,False)
        if tubeCollide:
        	self.playing = False

        if self.player.rect.y < 0:
        	self.playing = False



    def  draw(self):
        # Game Loop - draw
        # Drawing

        self.screen.blit(Background, [0,0])
        self.all_sprites.draw(self.screen)
        self.display_text(("Score:"+str(self.PLAYER_SCORE)),10,10,30,WHITE)
        self.display_text("Highscore:"+self.read[0],200,10,30,WHITE)
        #After everything has been drawn, flip the display
        pg.display.flip()



    def show_go_screen(self):
        # Game Over Screen
        gameStart = False
        while not gameStart:
        	self.display_text("Flappy Bird",WIDTH / 3, HEIGHT / 3, 30, WHITE)
        	self.display_text("Press S to Start...",WIDTH/3, HEIGHT / 2, 30, WHITE)
        	pg.display.flip()
        	for event in pg.event.get():
        		if event.type == pg.QUIT:
        			gameStart = True
        			self.running = False
        		if event.type == pg.KEYDOWN and event.key == pg.K_s:
        			gameStart = True

    def show_start_screen(self):
    	# Game Over Screen
        gameStart = False
        while not gameStart:
        	self.screen.blit(Background, [0,0])
        	self.display_text("Flappy Bird",WIDTH / 3, HEIGHT / 3, 30, WHITE)
        	self.display_text("Press S to Start...",WIDTH/3, HEIGHT / 2, 30, WHITE)
        	pg.display.flip()
        	for event in pg.event.get():
        		if event.type == pg.QUIT:
        			gameStart = True
        			self.running = False
        		if event.type == pg.KEYDOWN and event.key == pg.K_s:
        			gameStart = True

    def display_text(self,message,x,y,size,color):
        font = pg.font.SysFont("Comic Sans Ms", size)
        text = font.render(message,False,color)
        self.screen.blit(text,(x,y))


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.run()
    g.show_go_screen()
