import pygame

import printscreen
import game
import subblock
import block
import start
from constants import *


def main():
	over = False
	pygame.init()
	bgscreen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
	logo = pygame.image.load('images/logo.png').convert()
	font = pygame.font.SysFont("./Prettyfont.ttf", 35)
	pygame.display.set_caption('Tetris')
	# gameobj=game.Game()
	start.gameLoop(bgscreen,font,logo)


if __name__ == "__main__":
	main()  
