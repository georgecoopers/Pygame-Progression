import pygame as pg
import random
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):
	def __init__(self,imagePath):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(imagePath)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(WIDTH / 2, HEIGHT /2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def update(self):
		self.acc = vec(0,PLAYER_GRAV)
		self.vel += self.acc
		self.pos += self.vel +0.5 * self.acc
		self.rect.midbottom = self.pos


class Tube(pg.sprite.Sprite):
	def __init__(self,x,y,w,h,color):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velX = -5
		if self.rect.right < 0:
			self.kill()

	def update(self):
		self.rect.x += self.velX


class Ground(pg.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(SAND)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y