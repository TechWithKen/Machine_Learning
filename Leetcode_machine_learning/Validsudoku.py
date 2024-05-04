def no_repetition(array):
	"""Function to ensure that there is no repetition in every 1-9 numbers given"""
	no_repeat = []
	for i in array:
		if i == ".":
			pass
		else:
			no_repeat.append(i)
	if len(set(no_repeat)) != len(no_repeat):
		return False
	else:
		return True

def check_row(array):
	"""Function to check if all rows in the sudoku board are valid"""
	for i in array:
		if no_repetition(i) == False:
			return False
		else:
			continue
	return True

def collect_column(array, second_counter):
	"""Function to check if all the columns in the sudoku board are valid"""
	store = []
	counter = 0
	while counter < 9:
		store.append(array[counter][second_counter])
		counter += 1
	return store

def check_column(array):
	"""Function to check if all column in the sudoku board are valid"""
	for i in range(9):
		if no_repetition((collect_column(array, i))) == False:
			return False
		else:
			continue
	return True

def collect_three_by_three(array, start, stop, fnumber, snumber):
	"""Function to collect all three by three collection grid in the array"""
	store = []
	for i in range(fnumber, snumber + 1):
		store.append(array[start][i]), store.append(array[start + 1][i]), store.append(array[stop][i])
	return store


def check_three_by_three(array):
	"""Fuction to check if all three by three grid in the sudoku board are valid"""
	status = True
	first_number = 0
	second_number = 2
	while second_number < 9:
		fnumber = 0
		snumber = 2
		for i in range(3):
			status = status and no_repetition(collect_three_by_three(array, first_number, second_number, fnumber, snumber))
			fnumber= fnumber + 3
			snumber = snumber + 3
		first_number += 3
		second_number += 3
	return status

def check_sudoku_board(array):
	"""Final function to ensure that all the three conditions, row, column and three by three grid are met"""
	return check_row(array) and check_column(array) and check_three_by_three(array)

print(check_sudoku_board(board))