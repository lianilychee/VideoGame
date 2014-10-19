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
    def __init__(self,x,y,screen):
        self.speed = 1
        self.x = x
        self.y = y
        self.create_cloud()

    def create_cloud(self):
        self.image = pygame.image.load('images/cloud.png')
        self.image = pygame.transform.scale(self.image, (200,100))

    def animate_cloud(self):

        
        screen.blit(self.image, (WIDTH - self.x, self.y))

        while self.x != -250:

            # Render cloud in initial position.
            screen.blit(self.image,(self.x, self.y))

            # "Clear" cloud.
            screen.fill((135,206,250))

            # Move cloud.
            screen.blit(self.image,(self.x-self.speed, self.y))
            pygame.display.update()

            self.x = self.x-self.speed

    def move_cloud(self):
    ''' Update the position. '''


# main game loop
while True:
    screen.fill((135,206,250))

    cloud_list = [cloud(WIDTH,200,screen), cloud(WIDTH,100,screen)]

    for i in cloud_list:
        i.animate_cloud()



    # cloud0 = cloud(WIDTH,200,screen)
    # cloud0.animate_cloud()
    # cloud1 = cloud(WIDTH,400,screen)
    # cloud1.animate_cloud()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(50)