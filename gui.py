import pygame
import time
from sudoku import is_valid, find_next

pygame.init()
WINDOW_SIZE = [491, 491]
MARGIN = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")
fnt = pygame.font.SysFont("comicsans", 60)

def draw_board():
	screen.fill(BLACK)
	for i in range(5, 486, 54):
		for j in range(5, 486, 54):
			pygame.draw.rect(screen, WHITE, (i, j, 49, 49))


def update_board(sudoku_board, i, j):
	#update the digit at (i, j)
	row = 5 + 54 * j
	col = 5 + 54 * i
	if sudoku_board[i][j] == 0:
		pygame.draw.rect(screen, WHITE, (row, col, 49, 49))
	else:
		pygame.draw.rect(screen, WHITE, (row, col, 49, 49))
		digit = fnt.render(str(sudoku_board[i][j]), 1, BLACK)
		screen.blit(digit, (row + 12, col + 10))

def draw_initial_board(sudoku_board):
	for i in range(len(sudoku_board)):
		for j in range(len(sudoku_board[i])):
			update_board(sudoku_board, i, j)

def draw_rectangle(i, j, color):
	row = 5 + 54 * j
	col = 5 + 54 * i
	pygame.draw.rect(screen, color, (row, col, 49, 49), 1)


def solve_gui(sudoku_board)->bool:
	next_pos = find_next(sudoku_board)
	if next_pos == None:
		return True
	else:
		row = next_pos[0]
		col = next_pos[1]

	for number in range(1, 10):
		if is_valid(sudoku_board, row, col, number):
			sudoku_board[row][col] = number
			update_board(sudoku_board, row, col)
			draw_rectangle(row, col, GREEN)
			pygame.display.update()
			pygame.time.delay(100)

			if solve_gui(sudoku_board):
				return True

			sudoku_board[row][col] = 0
			update_board(sudoku_board, row, col)
			draw_rectangle(row, col, RED)
			#pygame.time.delay(100)
			#draw_rectangle(row, col, WHITE)
			pygame.display.update()
			pygame.time.delay(100)

	return False
				



#draw_board()
draw_initial_board(board)
solve_gui(board)

#main loop
done = True

while done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = False
	
	#displays the changes on the screen
	pygame.display.flip()


pygame.quit()
