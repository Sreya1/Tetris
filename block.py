import pygame
from random import randint
import numpy 

import subblock
import game
from constants import *

class Block():
	def __init__(self, grid, block_which = RANDOM, list=(NO_OF_COLS / 2 ,0)):
		self.list = list

		if(block_which == RANDOM):
			self.which = randint(1,7) 
		else: 
			self.which = block_which
		self.grid = grid 
		self.list_of_subblocks = []
		self.list_of_coordinates = []

		self.adjacent_down = []
		self.adjacent_right = []
		self.adjacent_left = [] 

		self.stopped = False
		self.keep_subblocks()
	
	def set_which(self, block_which):
		self.which = block_which
		for i in self.list_of_coordinates:
			self.grid.get_subblock(i).set_which(block_which)

	def set_stopped(self, stopped):
		self.stopped = stopped
		for i in self.list_of_coordinates:
			subblock = self.grid.get_subblock(i)
			subblock.set_stopped(stopped)

		if stopped:
			self.grid.update_score_fall()
			Sound=pygame.mixer.Sound("./sounds/music.wav")
			Sound.play()



	def set_list(self):
		temp = self.list_of_coordinates[0]
		self.list = temp


	def set_adjacent_coordinates(self):
		self.adjacent_down = []
		self.adjacent_left = []
		self.adjacent_right = []
		for i in self.list_of_coordinates:
			right_coord = (i[0]+1, i[1])
			down_coord = (i[0],i[1]+1)
			left_coord = (i[0]-1,i[1])
			self.get_adjacents(DIR_RIGHT).append(self.grid.get_valid_coord(right_coord))
			self.get_adjacents(DIR_DOWN).append(self.grid.get_valid_coord(down_coord))
			self.get_adjacents(DIR_LEFT).append(self.grid.get_valid_coord(left_coord))
		return True

	def reset_subblocks(self):
		self.stopped = False
		for i in self.list_of_coordinates:
			self.grid.get_subblock(i).reset()
		self.list_of_coordinates = []

	def get_coordinates(self):
		return self.list_of_coordinates

	def get_center(self):
		if (self.which == T or self.which == L2 or self.which == L1): return self.list_of_coordinates[1]
		elif(self.which == S1): return self.list_of_coordinates[0]
		return (self.list_of_coordinates[2])

	def get_which(self):
		temp = self.which
		return temp

	def get_adjacents(self, direction):
		if(direction == DIR_DOWN): return self.adjacent_down
		if(direction == DIR_LEFT): return self.adjacent_left
		if(direction == DIR_RIGHT): return self.adjacent_right

	def is_stopped(self):
		return self.stopped

	def is_valid_adjacents(self, coordinates):
		for i in coordinates:
			if i == -1: 
				return False
		for i in coordinates:
			if(self.grid.get_subblock(i).is_stopped()): 
				return False
		return True

	def rotate(self):
		if(self.which == SQUARE): return True
		center = self.get_center()
		rotated_coord = []
		for i in self.list_of_coordinates:
			centered_i = numpy.subtract(i, center)
			temp_coord = (centered_i[1]*-1,centered_i[0])
			rotated_coord.append((temp_coord[0]+center[0],temp_coord[1]+center[1]))
		
		for i in rotated_coord:
			temp_coord = self.grid.get_valid_coord(i)
			if(temp_coord == -1): return False
			if(self.grid.get_subblock(temp_coord).is_stopped()): return False

		self.keep_subblocks(rotated_coord)
		return True

	def move_left(self, spaces=1):
		move_list_of_coordinates = []

		if(self.is_valid_adjacents(self.get_adjacents(DIR_LEFT))==False):
			return 0

		move_list_of_coordinates = self.get_adjacents(DIR_LEFT)
		self.keep_subblocks(move_list_of_coordinates)
		return 1

	def instant_down(self, spaces=1):
		move_list_of_coordinates = []

		if(self.is_valid_adjacents(self.get_adjacents(DIR_DOWN))==False):
			self.set_stopped(True)
			return -1

		
		move_list_of_coordinates = self.get_adjacents(DIR_DOWN)
		self.keep_subblocks(move_list_of_coordinates)
		return 1

	def move_right(self, spaces=1):
		move_list_of_coordinates = []

		if(self.is_valid_adjacents(self.get_adjacents(DIR_RIGHT))==False):
			return 0

		move_list_of_coordinates = self.get_adjacents(DIR_RIGHT)
		self.keep_subblocks(move_list_of_coordinates)
		return 1


	def dropdown(self, m):
		if(self.instant_down()==-1): 
			return (self.grid.clear_rows(m))

	def draw(self):
		for i in self.list_of_subblocks:
			i.draw(screen)


	def keep_subblocks(self, list_of_coordinates=DEF):
		self.reset_subblocks()

		if(list_of_coordinates == DEF):

			if(self.which == LINE):
				self.line()
				
			elif(self.which == SQUARE):
				self.square()

			elif(self.which == T):
				self.t()	

			elif(self.which == S1):
				self.s1()
				
			elif(self.which == L1):
				self.l1()

			elif(self.which == S2):
				self.s2()
				
			elif(self.which == L2):
				self.l2()
				
		elif(list_of_coordinates!= DEF):
			self.list_of_coordinates = list_of_coordinates
			
		for i in self.list_of_coordinates:
			self.grid.get_subblock(i).set_which(self.which)
		
		self.set_list()
		self.set_adjacent_coordinates()

	def line(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))
		self.list_of_coordinates.append((self.list[0], self.list[1]+2))
		self.list_of_coordinates.append((self.list[0], self.list[1]+3))

	def square(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]+1))

	def s1(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]))
		self.list_of_coordinates.append((self.list[0]-1, self.list[1]+1))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))

	def l1(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))
		self.list_of_coordinates.append((self.list[0], self.list[1]+2))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]+2))

	def s2(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]+1))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]+2))

	def t(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))
		self.list_of_coordinates.append((self.list[0]+1, self.list[1]+1))
		self.list_of_coordinates.append((self.list[0]-1, self.list[1]+1))

	def l2(self):
		self.list_of_coordinates.append((self.list[0], self.list[1]))
		self.list_of_coordinates.append((self.list[0], self.list[1]+1))
		self.list_of_coordinates.append((self.list[0], self.list[1]+2))
		self.list_of_coordinates.append((self.list[0]-1, self.list[1]+2))


	