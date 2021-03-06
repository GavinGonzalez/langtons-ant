import pygame
from time import sleep
from random import randint
import sys
import numpy as np


pygame.init()
clock = pygame.time.Clock()

def draw_grid(screen_width, cell_num, surface):
	cell_width = screen_width//cell_num

	x = 0 
	y = 0

	for i in range(cell_num):

		x = x + cell_width
		y = y + cell_width

		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, screen_width))
		pygame.draw.line(surface, (255, 255, 255), (0, x), (screen_width, x))

def redrawWindow(surface):
	surface.fill((0, 0, 0))
	draw_grid(800, 80, surface)

def turn_right(dire):
	if(dire >= 3):
		dire = dire%3
		return dire

	else:
		dire = dire + 1
		return dire

def turn_left(dire):
	if(dire == 0):
		dire = 3
		return dire

	else:
		dire = dire-1
		return dire

def move_ant(x, y, dire):
	if(dire == 0):
		y = y-1

	if(dire == 1):
		x = x+1

	if(dire == 2):
		y = y+1

	if(dire == 3):
		x = x-1

	return (x, y)


def ant_pos(x, y, dire, game_grid):

	#up 0
	#right 1
	#down 2
	#left 3
	
	if(game_grid[x][y] == 1):
		game_grid[x][y] = 0
		dire = turn_left(dire)
		x, y = move_ant(x, y, dire)
		
		
		
	elif(game_grid[x][y] == 0):
		game_grid[x][y] = 1
		dire = turn_right(dire)
		x, y = move_ant(x, y, dire)
		
	
	return (x, y, dire)


def show_ant(x, y, cell_width, surface):
	pygame.draw.rect(surface, (100, 255, 100), (x*cell_width, y*cell_width, cell_width, cell_width))

def show_game_grid(game_grid, cell_width, num_cells, surface):
	for i in range(num_cells):
		for j in range(num_cells):
			if(game_grid[i][j] == 1):
				pygame.draw.rect(surface, (255, 255, 255), (i*cell_width, j*cell_width, cell_width, cell_width))



def main():

	ant_x = 40
	ant_y = 40
	cell_width = 10
	dire = 0
	game_grid = np.zeros((80, 80))
	x = 1

	screen = pygame.display.set_mode((800, 800))


	while(True):


		redrawWindow(screen)

		if(not(ant_y == 800 or ant_y == 0 or ant_x == 800 or ant_x == 0)):
			ant_x, ant_y, dire = ant_pos(ant_x, ant_y, dire, game_grid)
			
		

		show_game_grid(game_grid, cell_width, 80, screen)

		show_ant(ant_x, ant_y, cell_width, screen)

		
		
			

		pygame.display.update()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		clock.tick(60)


if __name__ == '__main__':
	main()
