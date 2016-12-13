import pygame

import block
import piece
import game
from constants import *

class Board():
	def __init__(self, cols, rows, size, color, loc=[0,0]):
		
		self.score = 0
		self.level = 1
		

		self.paused = False
		self.color = color
		self.loc = loc
		self.cols = cols
		self.rows = rows
		self.size = size
		self.list_of_blocks = []
		self.block_group = pygame.sprite.Group()
		self.large_text = pygame.font.SysFont("monospace",50)
		self.small_text = pygame.font.SysFont("monospace",25)

		
		for j in range(rows):
			for i in range(cols):
				new_block = block.Block(self, [i, j])
				self.list_of_blocks.append(new_block)
				self.block_group.add(new_block)

	def get_image_coord(self, col_num, row_num):
		return [self.loc[0]+self.size * col_num, self.loc[1]+self.size*row_num]

	
	def get_valid_coord(self,coord):
		if((0<= coord[0] < self.cols) and (0<= coord[1] < self.rows)):
			return coord
		return -1

	def get_block(self, coord):
		for i in self.list_of_blocks:
			if(i.is_block(coord)): 
				return i
		return False

	def get_cell_size(self):
		return self.size

	def update_score_remove(self):
		self.score += 100
		self.update_level_fall()
		


	def update_score_fall(self):
		self.score += 10

	def update_level_fall(self):
		self.level = self.score /  100 +     1

	def get_score(self):
		return self.score


	def get_level(self):
		return self.level

	def is_empty(self, x, y):
		for i in self.list_of_blocks:
			if(i.get_x() == x and i.get_y()==y): 
				return False
			else: 
				return True

	def is_row_full(self, row):
		for i in range(self.cols):
			if(self.get_block((i,row)).is_stopped()==False): 
				return False
		return True

	def get_score2(self):
		return self.score
	def clear_rows(self):
		for i in range(self.rows):
			if(self.is_row_full(i)):
				self.update_score_remove()
				self.dropdown(i)
				i = 0 
		return -1

	def is_game_over(self, bgscreen,font,m):
		Sound=pygame.mixer.Sound("./sounds/music.wav")
		for i in range(self.cols):
			if(self.get_block((i,0)).is_stopped()):
				self.paused = True
		if self.paused:
			Sound.play()
			return True
		else: 
			return False

	def reset_game(self):
		self.score = 0
		for i in self.list_of_blocks:
			i.reset()

	def pause(self, bgscreen, font, logo, m):
		self.paused = True
		m.Pause_Message()
		pygame.display.update()
		while(self.paused):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						self.paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
					elif event.key == pygame.K_r:
						self.score = 0
						
						game.gameLoop(bgscreen,font,logo)
		return True

	def dropdown(self, row):
		for j in reversed(range(row+1)):
			for i in range(self.cols):
				if(j>=1):
					block1 = self.get_block((i,j))
					block2 = self.get_block((i,j-1))
					block1.set_stopped(block2.get_stopped())
					block1.set_type(block2.get_type())
					block2.reset()

	def display_text(self, pytext, print_TEXT, location, bgscreen):
			label = pytext.render(print_TEXT, 1, WHITE)
			bgscreen.blit(label,location)

	def draw_blocks(self, bgscreen):
		for b in self.list_of_blocks:
			b.draw(bgscreen)

	