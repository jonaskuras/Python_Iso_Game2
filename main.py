import pygame
import sys
from pygame.locals import *
from game_stats import Settings
from game_tiles import Tiles
import maps as maps
import game_functions as gf


# initialize classes
pygame.init()
gs = Settings()
tiles = Tiles()

# set the display mode, window title and FPS clock
screen = pygame.display.set_mode((gs.screen_width, gs.screen_height), DOUBLEBUF)
pygame.display.set_caption('Isometric')
FPSCLOCK = pygame.time.Clock()

map_data = maps.map_select(1)
height_data = maps.height_select(1)

gf.draw_map(map_data, height_data, screen, gs, tiles)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    FPSCLOCK.tick(30)
