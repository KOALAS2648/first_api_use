import pygame as pg; pg.init()
import sys
from get_image import status_code, image
# creates the screen
WINH, WINW = 800, 800
screen = pg.display.set_mode((WINW,WINH))
#loads the image from the api
fox_image = pg.image.load(image)
# main game loop
RUNNING = True
while RUNNING:
    # checks if the user wnts to exit the pygame window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False
    pg.display.set_caption(str(status_code))
    pg.display.flip()
