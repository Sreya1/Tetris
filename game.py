import pygame

import subblock
import block
import start
from constants import *

class GamePlay(block.Block):
	def __init__(self,cols,rows,size,colour,list=[0,0]):
		self.cols = cols
		self.rows = rows
		self.size = size
		self.colour = colour
		self.list = list
		self.list_of_subblocks = []
		self.subblock_group = pygame.sprite.Group()
		self.score = 0
		self.times = 0
		self.level = 1
		self.paused = False
		for j in range(rows):
			for i in range(cols):
				new_subblock = subblock.Subblock(self, [i, j])
				self.list_of_subblocks.append(new_subblock)
				self.subblock_group.add(new_subblock)

	def get_subblock(self, coord):
		for i in self.list_of_subblocks:
			if(i.is_subblock(coord)): 
				return i
		return False

	def get_image_coord(self, column, row):
		s = self.size
		x = self.list[0]
		y = self.list[1]
		return [x + s * column, y + s * row]

	
	def get_valid_coord(self,coord):
		c0 = coord[0]
		c1 = coord[1]
		if((c0 >= 0 and c0 < self.cols) and (c1 >= 0 and c1 < self.rows)):
			return coord
		return -1


	def get_cell_size(self):
		return self.size

	def get_level(self):
		return self.level

	def get_score(self):
		return self.score

	def is_empty(self, x, y):
		for i in self.list_of_subblocks:
			if(i.get_x() == x and i.get_y()==y): 
				return False
			else: 
				return True

	def update_score_fall(self):
		self.score += 10

	def update_score_remove(self):
		self.score += 100
		self.times += 1
		if self.times >= 5 : 
			self.level+= 1
			self.times = 0
			return True
		return False

	def CheckRowFull(self, row):
		for i in range(self.cols):
			if(self.get_subblock((i,row)).is_stopped()==False): 
				return False
		return True

	def checkRowEmpty(self,row):
		for i in range(self.cols):
			if(self.get_subblock((i,row)).is_stopped()==True): 
				return False
		return True


	def clear_rows(self, m):
		for i in xrange(self.rows):
			if(self.CheckRowFull(i)):
				self.update_score_remove()
				for j in reversed(xrange(i+1)):
					for k in range(self.cols):
						if(j>=1):
							subblock1 = self.get_subblock((k,j))
							subblock2 = self.get_subblock((k,j-1))
							subblock1.set_stopped(subblock2.is_stopped())
							subblock1.set_which(subblock2.get_which())
							subblock2.reset()
				i = 0 
		return -1

	def is_game_over(self, bgscreen, font, m):
		for i in range(self.cols):
			if(self.get_subblock((i,0)).is_stopped()):
				self.paused = True
		if self.paused:
			return True
		else: 
			return False
	

	def reset_game(self):
		self.score = 0
		self.level = 1
		for i in self.list_of_subblocks:
			i.reset()

	def pause(self, bgscreen, font, logo, m):
		self.paused = True
		m.Pause_Message()
		pygame.display.update()
		while(self.paused):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						self.paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
					elif event.key == pygame.K_r:
						self.score = 0
						start.gameLoop(bgscreen,font,logo)
		return True

	def draw_subblocks(self, bgscreen):
		for i in self.list_of_subblocks:
			i.draw(bgscreen)

	