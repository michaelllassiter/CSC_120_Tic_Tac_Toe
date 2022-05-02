# Michael Lassiter
# 2022SP.CSC.120.0003 
# CSC 120 Lab 09, Part 1
# April 24, 2022
# Adjusted program after finding Joseph Parks' video
# May 1, 2022
# CSC 120 Lab 09, Part 2
# board is a list of 3 lists, with each of these lists being a list containing
# three single character elements.
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def main():
	# initialize values
	player_id = 1
	number_of_turns = 0
	print('*************************************')
	print('Shall we play a game of Tic-Tac-Toe?')
	print('*************************************')
	# loop until a win
	while check_win(player_id) == False and number_of_turns < 9:
		print_board()
		print(f'Player {player_id}, make your mark.')
		row = validate_entry(input('Enter value between 0 and 2: '))
		col = validate_entry(input('Enter value between 0 and 2: '))
		# loop until player selects empty spot
		while check_mark(row, col) == False:
			print('This space is not available. Please try again.')
			row = validate_entry(input('Enter value between 0 and 2: '))
			col = validate_entry(input('Enter value between 0 and 2: '))
		place_mark(row, col, player_id)
		number_of_turns = number_of_turns + 1
		if check_win(player_id) == False and player_id == 1:
			player_id = 2
		elif check_win(player_id) == False and player_id == 2:
			player_id = 1
	print_board()
	if check_win(player_id) == True:
		print('*************************************')
		print(f'Congratulations!  Player {player_id}, you win!')
		print('*************************************')
	else:
		print('*************************************')
		print('Game is a draw.  Good match players!')
		print('*************************************')

# This function tests entry
def validate_entry(val):
	while len(val) > 1 or val.isdigit() == False or int(val) < 0 or int(val) > 2:
		print('Invalid entry. Please try again')
		val = input('Enter value between 0 and 2: ')
	return int(val)
	
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
		board[row][col]='O'

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

# This function 
# Call the main function
if __name__ == '__main__':
	main()