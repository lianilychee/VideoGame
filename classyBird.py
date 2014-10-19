### Video Game

### Creating the bird and clouds

import pygame, sys
from pygame.locals import *
from random import randint

# Constants
WIDTH = 800
HEIGHT = 600

cloud_width = 200
cloud_height = 100

sprite_width = 50
sprite_height = 50

brick_width = randint(50,150)
brick_height = randint(50,150)

nest_width = 100
nest_height = 50


# Screen settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird!')



class cloud:
    ''' Cloud class; consists of initializing and animating object. '''

    def __init__(self,x,y,screen):
        self.speed = 1
        self.x = x
        self.y = y
        self.create_cloud()

    def create_cloud(self):
        ''' Initialize cloud with cloud image. '''
        self.image = pygame.image.load('images/cloud.png')
        self.image = pygame.transform.scale(self.image, (200,100))

    def move(self):
         self.x = self.x-self.speed

    def render(self):
        # Render cloud in initial position.
        screen.blit(self.image,(self.x, self.y))


class brick:
    ''' Brick class; consists of initializing and animating object. '''

    def __init__(self,x,y,screen):
        self.speed = 1
        self.x = x
        self.y = y
        self.create_brick()

    def create_brick(self):
        ''' Initialize cloud with brick image. '''
        self.image = pygame.image.load('images/brick.png')
        self.image = pygame.transform.scale(self.image, (200,100))

    def move(self):
         self.x = self.x-self.speed

    def render(self):
        # Render brick in initial position.
        screen.blit(self.image,(self.x, self.y))


# main game loop
cloud_list = [cloud(WIDTH,200,screen), cloud(WIDTH+200,100,screen)]

brick_list = [brick(WIDTH,100,screen), brick(WIDTH+200,300,screen)]

while True:
    screen.fill((135,206,250))

    for i in brick_list:
        i.render()
        i.move()

    for i in cloud_list:
        i.render()
        i.move()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(50)