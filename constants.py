import pygame
from colours import *
from dimensions import *

clock = pygame.time.Clock()

DIR_DOWN = 0
DIR_LEFT = 1
DIR_RIGHT = 2

RANDOM = -1
DEF = 0
LINE = 1
SQUARE = 2
S1 = 3
L1 = 4
T = 5
S2 = 6
L2 = 7

IMAGE_NAMES = ['defaultbg.png', 'blue.jpg', 'yellow.jpg', 'green.jpg', 'red.jpg', 'orange.jpg', 'deepblue.jpg', 'pink.jpg']
IMAGE_INDEX = {'DEF':0, 'LINE': 1, 'SQUARE': 2, 'S1': 3, 'L1': 4, 'T': 5, 'S2':6, 'L2': 7}
