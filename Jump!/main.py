import pygame as pg
import random
from settings import *
from sprites import *
class Game:
    def __init__(self):
        #Initialize Pygame and Create Window
        self.running = True
        self.gameOver = False
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        
    def new(self):
        # Start a New Game

        # Groups
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        # Player object
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.PLAYER_SCORE = 0

        # Platform Object 
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.platforms.add(p)
            self.all_sprites.add(p)

    

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if self.gameOver:
                self.show_go_screen()


    

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # Check if the player hits a platform
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        # If player reaches the top quarter of the screen the window scrolls up
        if self.player.rect.top < HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top > HEIGHT:
                    self.PLAYER_SCORE += 1
                    print(self.PLAYER_SCORE)
                    plat.kill()

        # Spawn New platforms

        while len(self.platforms) < 6:
            p = Platform(random.randint(10,700),-(random.randint(20,100)),PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY))
            self.platforms.add(p)
            self.all_sprites.add(p)

        if self.player.rect.top > HEIGHT:
            self.playing = False
    


    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    


    def  draw(self):
        # Game Loop - draw
        #Drawing

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.display_text(("Points:"+str(self.PLAYER_SCORE)),0,0,40,WHITE)
    
        #After everything has been drawn, flip the display
        pg.display.flip()



    def show_go_screen(self):
        # Game Over Screen
        gameOverLoop = False
        while not gameOverLoop:
            self.screen.fill(BLACK)
            self.display_text("Welcome to Jump",WIDTH/3+30,HEIGHT/4,30,WHITE)
            self.display_text("A and D to move left and right and SPACE to Jump",WIDTH/3-20,HEIGHT/3,15,WHITE)
            self.display_text("Press any button to continue...",WIDTH/3+50,HEIGHT*2/3,15,WHITE)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.KEYUP:
                    self.gameOver = False
                    gameOverLoop = True
                    self.new()

    def display_text(self,message,x,y,size,color):
        font = pg.font.SysFont("Comic Sans Ms", size)
        text = font.render(message,False,color)
        self.screen.blit(text,(x,y))


g = Game()
g.show_go_screen()

while g.running:
    g.new()
    g.run()
    g.show_go_screen()





