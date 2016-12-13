import pygame

from constants import *

class Messages():
	def __init__(self, bgscreen, font):
		self.font = font
		self.bgscreen = bgscreen
		self.colour = WEIRD
		self.local_font50 = pygame.font.Font("./Prettyfont.ttf", 35)
		self.local_font45 = pygame.font.Font("./Prettyfont.ttf", 30)
		self.local_font40 = pygame.font.Font("./Prettyfont.ttf", 25)
		self.local_font20 = pygame.font.Font("./Prettyfont.ttf", 10)

	def Start_Message(self):
		self.bgscreen.fill(self.colour)
		print_TEXT = self.local_font50.render('TETRIS', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 120,100])

		print_TEXT = self.local_font50.render('INSTRUCTIONS', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 150,200])
		
		pygame.draw.rect(self.bgscreen, BLACK, [100 , 300, 50, 50])
		print_TEXT = self.local_font45.render('A', True, WHITE)
		self.bgscreen.blit(print_TEXT, [110, 300])
		pygame.draw.rect(self.bgscreen, BLACK, [170 , 300, 50, 50])
		print_TEXT = self.local_font45.render('D', True, WHITE)
		self.bgscreen.blit(print_TEXT, [180, 300])

		print_TEXT = self.local_font45.render('to', True, BLACK)
		self.bgscreen.blit(print_TEXT, [260, 305])
		print_TEXT = self.local_font45.render(' MOVE', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [300, 305])

		pygame.draw.rect(self.bgscreen, BLACK, [550 , 300, 50, 50])
		print_TEXT = self.local_font45.render('S', True, WHITE)
		self.bgscreen.blit(print_TEXT, [560, 300])

		print_TEXT = self.local_font45.render('to', True, BLACK)
		self.bgscreen.blit(print_TEXT, [640, 305])
		print_TEXT = self.local_font45.render(' ROTATE', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [680, 305])

		pygame.draw.rect(self.bgscreen, BLACK, [220 , 380, 400, 50])
		print_TEXT = self.local_font45.render('Space Bar', True, WHITE)
		self.bgscreen.blit(print_TEXT, [340, 380])
		print_TEXT = self.local_font45.render('to', True, BLACK)
		self.bgscreen.blit(print_TEXT, [655, 385])
		print_TEXT = self.local_font45.render(' FALL', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [690, 385])
		print_TEXT = self.local_font20.render('*level up on clearing 5 rows', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [220, 440])
		
		print_TEXT = self.local_font45.render('Press ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [300,550])
		print_TEXT = self.local_font45.render(' Q ', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [390,550])
		print_TEXT = self.local_font45.render('to Quit', True, BLACK)
		self.bgscreen.blit(print_TEXT, [440,550])

		print_TEXT = self.local_font45.render('Press ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [300,500])
		print_TEXT = self.local_font45.render(' E ', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [390,500])
		print_TEXT = self.local_font45.render('to Start', True, BLACK)
		self.bgscreen.blit(print_TEXT, [440,500])

		pygame.display.update()

	def Pause_Message(self):
		w = SCREEN_W/2
		h = SCREEN_H
		pygame.draw.rect(self.bgscreen, DARKGREEN, [(SCREEN_W-w)/2 , (SCREEN_H-h)/2, w, h])
		print_TEXT = self.local_font50.render('GAME PAUSED', True, GREYGREEN)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 120, (SCREEN_H-h)/2 + 30])
		print_TEXT = self.local_font45.render('C', True, GREYGREEN)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 115, (SCREEN_H-h)/2 + 105])
		print_TEXT = self.local_font45.render(' to continue', True, WHITE)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 130, (SCREEN_H-h)/2 + 105])

		print_TEXT = self.local_font45.render('Q', True, GREYGREEN)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 115, (SCREEN_H-h)/2 + 205])
		print_TEXT = self.local_font45.render(' to quit', True, WHITE)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 130, (SCREEN_H-h)/2 + 205])

		print_TEXT = self.local_font45.render('R', True, GREYGREEN)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 115, (SCREEN_H-h)/2 + 305])
		print_TEXT = self.local_font45.render(' to restart', True, WHITE)
		self.bgscreen.blit(print_TEXT, [(SCREEN_W-w)/2 + 130, (SCREEN_H-h)/2 + 305])
		pygame.display.update()


	def End_Message(self, score, level):
		self.bgscreen.fill(self.colour)
		Sound=pygame.mixer.Sound("./sounds/music.wav")
		Sound.play()
		print_TEXT = self.local_font50.render('GAME OVER', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 120,150])

		print_TEXT = self.local_font40.render('Score is ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 130,250])
		print_TEXT = self.local_font40.render(str(score), True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 + 20,250])

		print_TEXT = self.local_font40.render('Level is ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 130,300])
		print_TEXT = self.local_font40.render(str(level), True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 + 20,300])

		print_TEXT = self.local_font40.render('Press ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 180,400])
		print_TEXT = self.local_font40.render(' Q ', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 100,400])
		print_TEXT = self.local_font40.render('to Quit', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 50,400])

		print_TEXT = self.local_font40.render('Press ', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 180,450])
		print_TEXT = self.local_font40.render(' R ', True, SCREENTEXT)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 100,450])
		print_TEXT = self.local_font40.render('to Restart', True, BLACK)
		self.bgscreen.blit(print_TEXT, [SCREEN_W/2 - 50,450])

		pygame.display.update()


