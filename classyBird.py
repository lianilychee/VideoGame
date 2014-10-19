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

        #screen.blit(self.image, (WIDTH - self.x, self.y))

        # while self.x != -250:

        # Render cloud in initial position.
        screen.blit(self.image,(self.x, self.y))

        # "Clear" cloud.
        # screen.fill((135,206,250))

# class brick:

#     def __init__(self,x,y,screen):
#         self.speed = 1
#         self.x = x
#         self.y = y
#         self.create_brick()

#     def create_brick(self):

#         self.image = pygame.image.load('images/brick.png')
#         self.image = pygame.transform.scale(self.image, (200,100))

    
#     def move(self):
#          self.x = self.x-self.speed
#          print self.x
#          print self.speed

#     def render(self):

#         screen.blit(self.image, (WIDTH - self.x, self.y))

#         # while self.x != -250:

#         # Render cloud in initial position.
#         screen.blit(self.image,(self.x, self.y))

#         # "Clear" cloud.
#         screen.fill((135,206,250))

#         # Move cloud.
#         screen.blit(self.image,(self.x-self.speed, self.y))

#         self.move()


# main game loop
cloud_list = [cloud(WIDTH,200,screen), cloud(WIDTH+200,100,screen)]

while True:
    screen.fill((135,206,250))

    
    # brick_list = [brick(WIDTH,100,screen), brick(WIDTH,300,screen)] 

    # for i in brick_list:
    #     i.render()
    #     i.move()

    for i in cloud_list:
        i.render()
        i.move()

    pygame.display.update()





    # cloud0 = cloud(WIDTH,200,screen)
    # cloud0.animate_cloud()
    # cloud1 = cloud(WIDTH,400,screen)
    # cloud1.animate_cloud()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(50)