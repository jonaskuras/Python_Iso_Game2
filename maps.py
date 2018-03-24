import pygame
import os

def map_select(map_num):
    #the data for the map expressed as [row[tile]].
    if map_num == 1:
        map_data = [
            [2, 1, 1, 1, 1, 1],
            [2, 1, 0, 0, 1],
            [2, 1, 0, 1, 1],
            [2, 1, 1, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0]
            ]
        return(map_data)

def height_select(map_num):
    #the height data for the map expressed as [row[tile]].
    if map_num == 1:
        height_data = [
            [0, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 1],
            [1, -3, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [-1, 1, 0, 0, 1],
            [-2, -2, -1, 0, 0]
            ]
        return(height_data)
