def is_valid(sudoku_board, i, j, num)->bool:
	"""returns wether if num can be placed at position (i, j)"""
	
	for idx in range(0, 8):
		if sudoku_board[idx][j] == num:
			return False


	for idx in range(0, 8):
		if sudoku_board[i][idx] == num:
			return False

	row = int(i / 3)
	col = int(j / 3)

	for idx in range(row * 3, row * 3 + 3):
		for j in range(col * 3, col * 3 + 3):
			if sudoku_board[idx][j] == num:
				return False

	return True

def check_board(sudoku_board)->bool:
	"""checks wether the board is valid or not"""

	frecv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(sudoku_board)):
		for j in range(len(sudoku_board[i])):
			if sudoku_board[i][j] == 0:
				return False
			else:
				frecv[sudoku_board[i][j]] = frecv[sudoku_board[i][j]] + 1

	for idx in range(len(frecv)):
		if idx != 0 and frecv[idx] != 1:
			return False

	for idx in range(len(frecv)):
		frecv[idx] = 0

	for i in range(len(sudoku_board)):
		for j in range(len(sudoku_board[i])):
			if sudoku_board[j][i] == 0:
				return False
			else:
				frecv[sudoku_board[j][i]] = frecv[sudoku_board[j][i]] + 1

	for idx in range(len(frecv)):
		if idx != 0 and frecv[idx] != 1:
			return False


	for idx in range(len(frecv)):
		frecv[idx] = 0


	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			for idx in range(len(frecv)):
				frecv[idx] = 0
			for i in range(row, row + 2):
				for j in range(col, col + 2):
					frecv[sudoku_board[i][j]] = frecv[sudoku_board[i][j]] + 1
			for idx in range(len(frecv)):
				if idx != 0 and frecv[idx] != 0:
					return False

	return True

def find_next(sudoku_board)->tuple:
	for i in range(len(sudoku_board)):
		for j in range(len(sudoku_board[i])):
			if sudoku_board[i][j] == 0:
				return (i, j)
	return None

def solve(sudoku_board)->bool:
	next_pos = find_next(sudoku_board)
	if next_pos == None:
		return True
	else:
		row = next_pos[0]
		col = next_pos[1]

	for number in range(1, 10):
		if is_valid(sudoku_board, row, col, number):
			sudoku_board[row][col] = number

			if solve(sudoku_board):
				return True

			sudoku_board[row][col] = 0

	return False

def print_board(sudoku_board):
	for i in range(len(sudoku_board)):
		for j in range(len(sudoku_board[i])):
			print(sudoku_board[i][j], end = " ")
		print("\n")


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

	
#print_board(board)
#solve(board)
#print_board(board)
