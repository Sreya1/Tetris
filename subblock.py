import pygame

from constants import *

class Subblock(pygame.sprite.Sprite):
	def __init__(self, grid, list=[0,0], block_which = DEF):
		
		pygame.sprite.Sprite.__init__(self)
		self.grid = grid
		self.list = list
		self._which = block_which        # Private data members
 		self._stopped = False

		self.image_list = []
		
		for i in IMAGE_NAMES:
			temp_image = pygame.image.load('images/'+i).convert()
			temp_image = pygame.transform.scale(temp_image, (int(self.grid.get_cell_size()), int(self.grid.get_cell_size())))
			self.image_list.append(temp_image)

		self.image = self.image_list[DEF]
		self.rect = self.image.get_rect()
        
		self.coord = self.grid.get_image_coord(self.list[0], self.list[1])
		self.rect.x = self.coord[0]
		self.rect.y = self.coord[1]

	def get_which(self):
		return self._which

	def is_stopped(self):
		return self._stopped

	def set_stopped(self, stopped):
		self._stopped = stopped
	def set_which(self, block_which):
		self._which = block_which
	
	def set_x_loc(self,x):
		self.list[0] = x
	def set_y_loc(self,y):
		self.list[1] = y
	
	def reset(self):
		self.set_which(DEF)
		self.set_stopped(False)

	def is_subblock(self,list):
		if(self.list[0] == list[0] and self.list[1] == list[1]): 
			return True
		else: 
			return False

	def load_image(self):
		self.image = self.image_list[self._which]
		self.image = pygame.transform.scale(self.image, (int(self.grid.get_cell_size())-2, int(self.grid.get_cell_size())-2))
		self.rect = self.image.get_rect()

	def draw(self, bgscreen):
		self.load_image()
		self.coord = self.grid.get_image_coord(self.list[0], self.list[1])
		self.rect.x = self.coord[0]
		self.rect.y = self.coord[1]
		bgscreen.blit(self.image, (self.rect.x, self.rect.y))
