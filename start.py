import pygame

import printscreen
import game
import subblock
import block
from constants import *

def event_handling(fallingBlock, boardgrid, bgscreen, font, logo, m):
	for event in pygame.event.get():
			
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
		
			elif event.key == pygame.K_s:
				fallingBlock.rotate()
			elif event.key == pygame.K_p:
				boardgrid.pause(bgscreen,font,logo,m)

			else:
				pass
					
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		fallingBlock.move_left()
	elif keys[pygame.K_d]:
		fallingBlock.move_right()
	elif keys[pygame.K_SPACE]:
		fallingBlock.instant_down()
	else:
		pass

def gameLoop(bgscreen,font,logo):
	
	m = printscreen.Messages(bgscreen, font)

	begin = False
	over = False
	m.Start_Message()
	while not begin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_e:
					begin = True
				elif event.key == pygame.K_q:
					begin = True
					over = True

	boardgrid = game.GamePlay(NO_OF_COLS, NO_OF_ROWS, int((SCREEN_H-BORDER)/NO_OF_ROWS), BLACK, [BOARD_X, BORDER/2])

	nextGrid = game.GamePlay(4, 4, int((SCREEN_H-BORDER)/NO_OF_ROWS), BLACK, [NEXT_X, BORDER/2])
	fallingBlock = block.Block(boardgrid)
	nextPiece = block.Block(nextGrid, list=[1,0])

	while not over:
		bgscreen.fill(GREYGREEN)
		bgscreen.blit(logo, LOGO_POS)

		local_font = pygame.font.Font("./Prettyfont.ttf", 20)
		print_TEXT = local_font.render('Level: {}'.format(boardgrid.get_level()), True, DARKGREEN)
		bgscreen.blit(print_TEXT, [20,200])
		print_TEXT = local_font.render('Score: {}'.format(boardgrid.get_score()), True, DARKGREEN)
		bgscreen.blit(print_TEXT, [20,150])
		print_TEXT = local_font.render("Next ", True, DARKGREEN)
		bgscreen.blit(print_TEXT, [NEXT_X, 100])

		event_handling(fallingBlock,boardgrid,bgscreen,font,logo,m)
					
		drop_loop = fallingBlock.dropdown(m)

		if(drop_loop == -1):
			if(boardgrid.is_game_over(bgscreen,font,m)): 
				over = True
			
			fallingBlock = block.Block(boardgrid, nextPiece.get_which())
			nextPiece.reset_subblocks()
			nextPiece = block.Block(nextGrid, list=[1,0])

		nextGrid.draw_subblocks(bgscreen)
		boardgrid.draw_subblocks(bgscreen)

		pygame.display.update()

		while over == True:
			finalscore = boardgrid.get_score()
			finallevel = boardgrid.get_level()

			m.End_Message(finalscore,finallevel)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
					if event.key == pygame.K_r:
						over = False
						begin = False
						gameLoop(bgscreen, font, logo)
	
		clock.tick(8 + boardgrid.get_level())
	pygame.quit()



