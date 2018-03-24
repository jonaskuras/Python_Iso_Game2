import pygame
import time
import os 

class Tiles():
    def __init__(self):
        """Initialize the games tiles"""
        self.floor = pygame.image.load(os.path.join('images','floor.png'))
        self.wall_l = pygame.image.load(os.path.join('images','wall_l.png'))
        self.blank = pygame.image.load(os.path.join('images','blank.png'))