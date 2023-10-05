import pygame
import time

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, horizontal, vertical, width, height, image):
		self.x = horizontal
		self.y = vertical
		self.w = width
		self.h = height
		self.image = pygame.image.load(image)
	def isGoomba(self):
		return False

	def isMario(self):
		return False

	def isPipe(self):
		return False

	def isFireball(self):
		return False

class Fireball(Sprite):
	def __init__(self, horizontal, vertical):
		super().__init__(horizontal,vertical,47,47,"fireball.png")
		self.x = horizontal
		self.y = vertical
		self.px = horizontal
		self.py = vertical
		self.vertVelocity = 0
		self.bounceNumber = 0
		self.directionSwitch = False
		self.image = pygame.image.load("fireball.png")
	
	def isMario(self):
		return False
	
	def isPipe(self):
		return False
	
	def isGoomba(self):
		return False
	
	def isFireball(self):
		return True

	def update(self):
		if (self.directionSwitch == True):
			self.x += 10
			self.vertVelocity += 1.2
			self.y += 4 + self.vertVelocity
		elif (self.directionSwitch == False):
			self.x += 10
			self.vertVelocity += 1.2
			self.y += -10 + self.vertVelocity
		if(self.y > 760 or ((self.y < self.py - 50) and self.bounceNumber == 0) or (self.y < 20 and self.bounceNumber == 0) or (self.y < 400 and self.bounceNumber != 0)):
			if (self.y > 760):
				self.bounceNumber = self.bounceNumber + 1
			self.y = 760
			self.vertVelocity = 0
			self.directionSwitch =  not self.directionSwitch

class Mario(Sprite):
	def __init__(self):
		super().__init__(0,0,60,95,"mario1.png")
		self.px = 0
		self.py = 0
		self.vertVelocity = 0
		self.numFramesInAir = 0
		self.marioMoving = False
		self.x = 0
		self.y = 0
		self.drawingCounter = 0
		self.w = 60
		self.h = 95
		self.imageArray = [pygame.image.load("mario1.png"), pygame.image.load("mario2.png"), pygame.image.load("mario3.png"), pygame.image.load("mario4.png"), pygame.image.load("mario5.png")]

	def isMario(self):
		return True
	
	def isPipe(self):
		return False
	
	def isGoomba(self):
		return False
	
	def isFireball(self):
		return False

	def update(self):
		self.numFramesInAir = self.numFramesInAir + 1
		self.vertVelocity += 1.2
		self.y += self.vertVelocity

		if(self.y > 710):
			self.vertVelocity = 0
			self.y = 710
			self.numFramesInAir = 0

		if(self.marioMoving == True):
			self.drawingCounter = self.drawingCounter + 1
			if (self.drawingCounter == 5):
				self.drawingCounter = 0
			self.image = self.imageArray[self.drawingCounter]
		else:
			self.image = self.imageArray[0]
		
	def setPreviousPosition(self):
		self.px = self.x
		self.py = self.y

	def getOutOfPipeX(self):
		self.x = self.px

	def getOutOfPipeY(self):
		self.y = self.py
		self.vertVelocity = 0

class Pipe(Sprite):
	def __init__(self, horizontal, vertical):
		super().__init__(horizontal,vertical,55,400,"pipe.png")
		self.x = horizontal
		self.y = vertical
		self.w = 55
		self.h = 400
		self.image = pygame.image.load("pipe.png")
	
	def isMario(self):
		return False
	
	def isPipe(self):
		return True
	
	def isGoomba(self):
		return False
	
	def isFireball(self):
		return False

class Goomba(Sprite):
	def __init__(self, horizontal, vertical):
		super().__init__(horizontal,vertical,37,45,"goomba.png")
		self.x = horizontal
		self.y = vertical
		self.vertVelocity = 0
		self.bounceNumber = 0
		self.directionSwitch = False
		self.h = 37
		self.w = 45
		self.px = horizontal
		self.py = vertical
		self.movingActivated = True
		self.numFrames = 0
		self.image = pygame.image.load("goomba.png")
	
	def isMario(self):
		return False
	
	def isPipe(self):
		return False
	
	def isGoomba(self):
		return True
	
	def isFireball(self):
		return False

	def update(self):
		if (self.movingActivated == False):
			self.numFrames = self.numFrames + 1
			self.image = pygame.image.load("goomba_fire.png")
		if (self.directionSwitch == True and self.movingActivated == True):
			self.x -= 4
		elif (self.movingActivated == True):
			self.x += 4
		self.vertVelocity += 1.2
		self.y += self.vertVelocity

		if(self.y > 760):
			self.vertVelocity = 0
			self.y = 760
	
	def setPreviousPosition(self):
		self.px = self.x
		self.py = self.y

	
	def getOutOfPipeX(self):
		self.x = self.px
		self.directionSwitch = not self.directionSwitch

	def getOutOfPipeY(self):
		self.y = self.py
		self.vertVelocity = 0

class Model():
	def __init__(self):
		self.Mario = Mario()
		self.sprites = []
		self.Pipe1 = Pipe(200, 200)
		self.Pipe2 = Pipe(400, 500)
		self.sprites.append(self.Mario)
		self.sprites.append(self.Pipe1)
		self.sprites.append(self.Pipe2)
		self.sprites.append(Pipe(150,400))
		self.sprites.append(Pipe(300,50))
		self.sprites.append(Pipe(314,42))
		self.dest_x = 0
		self.dest_y = 0


		self.sprites = []
		self.mario = Mario()
		self.sprites.append(self.mario)
		self.sprites.append(Pipe(200, 250))
		self.sprites.append(Pipe(500, 700))
		self.sprites.append(Pipe(800, 700))
		self.sprites.append(Goomba(600, 300))
		self.sprites.append(Goomba(620, 300))
		self.sprites.append(Goomba(580, 300))
		self.check = False
		self.checkGoomba = False
	
	def update(self):
		for sprite in self.sprites:
			if (sprite.isGoomba()):
				if (((sprite).movingActivated == False) and (((sprite).numFrames >= 50))):
					self.sprites.remove(sprite)
			elif ((sprite.isFireball())):
				if ((sprite).x > ((sprite).px + 3000)):
					self.sprites.remove(sprite)
		for sprite in self.sprites:
			if (sprite.isPipe() == False):
				sprite.update()
		for sprite in self.sprites:
			if ((sprite).isPipe()):
				self.check = self.areColliding(self.mario,(sprite))
				for item in self.sprites:
					if (item.isGoomba()):
						self.checkGoomba = self.areColliding(item, sprite)
						if (self.checkGoomba) and (((item)).py + ((item)).h <= ((sprite).y)):
							((item)).getOutOfPipeY()
						elif (self.checkGoomba):
							((item)).getOutOfPipeX()
			if ((self.check == True) and (sprite.isPipe())):
				if (self.mario.py + self.mario.h <= ((sprite).y)) or (self.mario.py >= ((sprite).y + ((sprite).h))):
					if (self.mario.py + self.mario.h <= ((sprite).y)):
						self.mario.numFramesInAir = 0
					self.mario.getOutOfPipeY()
				else:
					self.mario.getOutOfPipeX()
			if (sprite.isFireball()):
				for item in self.sprites:
					if(item.isGoomba()):
						self.checkGoomba = self.areColliding(item, sprite)
						if ((self.checkGoomba == True) and (((item)).movingActivated == True)):
							((item)).movingActivated = False
							self.sprites.remove(sprite)
							break
		
	def areColliding(self, q, p):
		if(q.x + q.w < p.x):
			return False
		if(q.x > p.x + p.w):
			return False
		if(q.y + q.h < p.y):
			return False
		if(q.y > p.y + p.h):
			return False
		return True

class View():
	def __init__(self, model):
		screen_size = (1500,1500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.model = model
		self.scrollPos = self.model.mario.x - 2*self.model.mario.w
		self.color = (0,0,255)
		#self.model.rect = self.Mario_image.get_rect()

	def update(self):    
		self.scrollPos = self.model.mario.x - 2*self.model.mario.w
		self.screen.fill([0,200,100])
		#self.screen.blit(self.Mario_image, self.model.rect)
		for sprite in self.model.sprites:
			self.screen.blit(sprite.image, (sprite.x - self.scrollPos, sprite.y))
		# self.screen.blit(self.model.Mario.image, (self.model.Mario.x, self.model.Mario.y))
		# self.screen.blit(self.model.Pipe1.image, (self.model.Pipe1.x, self.model.Pipe1.y))
		# self.screen.blit(self.model.Pipe2.image, (self.model.Pipe2.x, self.model.Pipe2.y))
		pygame.draw.rect(self.screen, self.color, pygame.Rect(0, 800, 1500, 1500))
		pygame.display.flip()
	
	def setModel(self, m):
		self.model = m

class Controller():
	def __init__(self, model):
		self.model = model
		self.key_right = False
		self.key_left = False
		self.key_up = False
		self.key_down = False
		self.key_space = False
		self.isMoving = False
		self.keep_going = True
		self.scrollContPos = self.model.mario.x - 2*self.model.mario.w
	
	def setModel(self, m):
		self.model = m

	def update(self):
		self.scrollContPos = self.model.mario.x - 2*self.model.mario.w
		self.model.mario.marioMoving = self.isMoving
		self.model.mario.setPreviousPosition()
		for sprite in self.model.sprites:
			if (sprite.isGoomba()):
				(sprite).setPreviousPosition()
		if (self.key_right):
			self.scrollContPos = self.model.mario.px - 2*self.model.mario.w
			self.isMoving = True
			self.model.mario.x += 4
			self.model.mario.marioMoving = self.isMoving
		if (self.key_left):
			self.scrollContPos = self.model.mario.px - 2*self.model.mario.w
			self.isMoving = True
			self.model.mario.x -= 4
			self.model.mario.marioMoving = self.isMoving
		if (self.key_space and self.model.mario.numFramesInAir < 5):
			self.model.mario.vertVelocity += -5

		for event in pygame.event.get():
			if (event.type == KEYDOWN):
				self.keys = pygame.key.get_pressed()
				if self.keys[K_LEFT]:
					self.key_left = True
				if self.keys[K_RIGHT]:
					self.key_right = True
				if self.keys[K_UP]:
					self.key_up = True
				if self.keys[K_DOWN]:
					self.key_down = True
				if self.keys[K_SPACE]:
					self.key_space = True
				if self.keys[K_LCTRL]:
					self.model.sprites.append(Fireball(self.model.mario.x, self.model.mario.y))
				if (event.key == pygame.K_ESCAPE):
					self.keep_going = False
			elif (event.type == KEYUP):
				if (event.key == pygame.K_LEFT):
					self.key_left = False
					self.isMoving = False
				if (event.key == pygame.K_RIGHT):
					self.key_right = False
					self.isMoving = False
				if (event.key == pygame.K_UP):
					self.key_up = False
				if (event.key == pygame.K_DOWN):
					self.key_down = False
				if (event.key == pygame.K_SPACE):
					self.key_space = False
			elif event.type == QUIT:
				self.keep_going = False

print("Use the arrow keys to move, space to jump, and lctrl to shoot fireballs. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")