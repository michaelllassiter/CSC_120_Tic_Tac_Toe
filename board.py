# Michael Lassiter
# 2022SP.CSC.120.0003 
# CSC 120 Lab 09
# Adjusted program after finding Joseph Parks' video
# board is a list of 3 lists, with each of these lists being a list containing
# three single character elements.
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def main():
	print()
	# Call print_board() for test
	print('print_board() unit test:')
	print_board()
	print()
	# Call check_mark() for test
	print('check_mark(1,1) test:')
	print(check_mark(1, 1))
	print()
	# Call place_mark() for test
	print('place_mark(1,1,1) test:')
	place_mark(1,1,1)
	print_board()
	# Call check_win for test
	print('check_win(1) test:')
	print(check_win(1))
	
# This function prints the board as a tic-tak-toe board
def print_board():
	# board is a list of 3 lists
	print('Printing board...')
	for row in board:
		print(row)

# If board[row][col] equals '-' check_mark returns True.
# Otherwise it returns False.
def check_mark(row, col):
	if board[row][col] == '-':
		result = True
	else:
		result = False
	return result

# This function does the following:
# if player_id equals 1, board[row][col] is set to 'X'
# if player_id equals 2, board[row][col] is set to 'O'
def place_mark(row, col, player_id):
	if player_id == 1:
		board[row][col]='X'
	if player_id == 2:
		board[row][col]='Y'

# This function does the following:
# if player_id equals 1, the function checks if any row, column or diagonal
# contains all 'X' characters.
# If so, the function returns True.  Otherwise the function returns False.
# if player_id equals 2, the function checks if any row, column or diagonal
#  contains all 'O' characters.
# If so, the function returns True.  Otherwise the function returns False.
def check_win(player_id):
	# initialize result
	result = False
	# set test_value
	if player_id == 1:
		test_value = ['X', 'X', 'X']
	else:
		test_value = ['O', 'O', 'O']
	# test rows for win
	for i in range(3):
		if board[i] == test_value:
			result = True
	# test columns for win
	for i in range(3):
		if [board[0][i], board[1][i], board[2][i]] == test_value:
			result = True
	# test diagonals for win
	# top left to bottom right
	if [board[0][0], board[1][1], board[2][2]] == test_value:
		result = True
	# bottom left to top right
	if [board[2][0], board[1][1], board[0][2]] == test_value:
		result = True
	return result
	
# Call the main function
if __name__ == '__main__':
	main()