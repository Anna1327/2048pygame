import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()
width=500
height=500
mainSurface=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Keyb moves')

background=pygame.image.load('0.png')

sprite=pygame.image.load('0.png') # Create moving image

# Place image to the center of mainSurface
spritex=(mainSurface.get_width() - sprite.get_width())/2
spritey=(mainSurface.get_height() - sprite.get_height())/2
direction=False

# --->
def move(direction, spritex, spritey):
    # This function moves recalculates new image coordinates
    if direction:
        if direction == K_UP:
            spritey-=5
        elif direction == K_DOWN:
            spritey+=5
        if direction == K_LEFT:
            spritex-=5
        elif direction == K_RIGHT:
            spritex+=5
    return spritex, spritey
# --->

# game loop
while True:
    fpsClock.tick(FPS) # define frame rate
    mainSurface.blit(background,(0,0))
    mainSurface.blit(sprite,(spritex,spritey))

    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue, remember in 'direction' pressed key code
        if event.type==QUIT:
            # window close X pressed
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and event.key == K_ESCAPE:
            # ESC key pressed
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: direction = event.key # Other key pressed
        if event.type == KEYUP:  direction = False # Key released

    # calculate new image position
    spritex, spritey = move(direction, spritex, spritey)

    pygame.display.update()