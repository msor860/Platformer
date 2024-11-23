import pygame, sys
import os
from pygame.locals import QUIT

pygame.init()

#Do something new idk

WIDTH = 500
HEIGHT = 500

canLeft = True
canRight = True
 
gravity = 0.01

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
WHITE = (255, 255, 255)
GREEN = (100, 255, 100)
PURPLE = (200, 0, 255)
BACK = (230, 230, 255)
SKY = (175, 200, 255)
font = pygame.font.Font('freesansbold.ttf', 64)

background = pygame.Rect(0, 0, 500, 500)
ground = pygame.Rect(0, 450, 500, 30)


class Player():

    def __init__(self):
        self.rect = pygame.Rect(30, 400, 50, 50)
        self.xPos = 30
        self.yPos = 400
        self.xSpeed = 1
        self.ySpeed = 0
        self.inAir = False

    def draw(self):
        self.rect = pygame.Rect(self.xPos, self.yPos, 50, 50)
        pygame.draw.rect(DISPLAYSURF, RED, self.rect)

    def jump(self, x):
        if self.inAir == False:
            self.ySpeed = x
            self.inAir = True


class thruBlock():

    def __init__(self):
        self.rect = pygame.Rect(-20, -20, 10, 10)
        self.xPos = 0
        self.yPos = 0
        self.width = 0
        self.height = 0

    def createBlock(self, xPos, yPos, xSize, ySize):
        self.rect = pygame.Rect(xPos, yPos, xSize, ySize)
        self.xPos = xPos
        self.yPos = yPos
        self.width = xSize
        self.height = ySize
        pygame.draw.rect(DISPLAYSURF, YELLOW, self.rect)


class Block(thruBlock):

    def createBlock(self, xPos, yPos, xSize, ySize):
        self.rect = pygame.Rect(xPos, yPos, xSize, ySize)
        self.xPos = xPos
        self.yPos = yPos
        self.width = xSize
        self.height = ySize
        pygame.draw.rect(DISPLAYSURF, PURPLE, self.rect)


player = Player()
thrublock = thruBlock()
thrublock2 = thruBlock()
allBlocks = [thrublock, thrublock2]
block = Block()

DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Platformer')
while True:
    pygame.draw.rect(DISPLAYSURF, SKY, background)
    pygame.draw.rect(DISPLAYSURF, GREEN, ground)
    player.draw()
    thrublock.createBlock(0, 350, 150, 25)
    thrublock2.createBlock(0, 250, 150, 25)
    block.createBlock(350, 340, 150, 50)
    if player.xPos <= 0:
        player.xPos = 0
    if player.xPos >= 450:
        player.xPos = 450
    if player.inAir:
        SKY = (255, 140, 0)
        player.yPos -= player.ySpeed
        player.ySpeed -= gravity
    else:
        SKY = (175, 200, 255)
    if pygame.Rect.colliderect(player.rect, ground):
        player.inAir = False
    for thrublock in allBlocks:
      if pygame.Rect.colliderect(player.rect, thrublock.rect):
          GREEN = (255, 255, 0)
          if player.yPos + 45 <= thrublock.yPos:
              if (player.xPos + 50) >= thrublock.xPos and player.xPos <= (
                      thrublock.xPos + thrublock.width):
                  player.inAir = False
              else:
                  player.inAir = True
          elif player.yPos >= (thrublock.yPos + thrublock.height):
              player.ySpeed = 0
          else:
              if (player.xPos + 50) >= thrublock.xPos:
                  pass
              if player.xPos <= (thrublock.xPos + thrublock.width):
                  pass
  
    if pygame.Rect.colliderect(player.rect, block.rect):
        GREEN = (255, 255, 0)
        if player.yPos + 45 <= block.yPos:
            if (player.xPos + 50) >= block.xPos and player.xPos <= (
                    block.xPos + block.width):
                player.inAir = False
            else:
                player.inAir = True
        elif player.yPos + 5 >= (block.yPos + block.height):
            player.ySpeed = 0
            player.yPos += 1
        else:
            if (player.xPos + 50) >= block.xPos:
                canLeft = False
                canRight = True
                player.xSpeed = 0
                player.xPos -= 1
                player.xSpeed = 1
            if player.xPos <= (block.xPos + block.width):
                canLeft = True
                canRight = False
                player.xSpeed = 0
                player.xPos -= 1
                player.xSpeed = 1

    else:
        if not pygame.Rect.colliderect(player.rect, ground):
            GREEN = (100, 255, 100)
            player.inAir = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if canLeft:
            player.xPos -= player.xSpeed
            canRight = True
    elif keys[pygame.K_d]:
        if canRight:
            player.xPos += player.xSpeed
            canLeft = True
    if keys[pygame.K_SPACE]:
        player.jump(1.5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #if canLeft == False:
    #  print("noLeft")
    #if canRight == False:
    #  print("noRight")
    pygame.display.update()
    clock.tick(300)
