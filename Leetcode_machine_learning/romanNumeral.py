roman_numeral = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, 
				"XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, 
				"V": 5, "IV": 4, "I": 1, }

def convert_to_list(int_value:int):
	"""Convert user entry to a list to begin execution"""
	convert_number_to_string = str(collect_number)
	convert_to_list = list(convert_number_to_string)
	return convert_to_list

def get_standard_form(array):
	"""get the highest power and turn to standard form"""
	individual_value_list = []
	power_dictionary = {"4": 1000, "3": 100, "2": 10, "1": 1}
	for i in range(len(array)):
		individual_value_list.append(int(array[i]) * power_dictionary[str(len(array) -  i)])

	return individual_value_list

def get_roman_numeral(array):
	"""Get the final roman numeral equivalent of a given intger value"""
	for i in array:
		for j in roman_numeral:
			if i % roman_numeral[j] == 0 and i // roman_numeral[j] <= 3:
				print(j * (i // roman_numeral[j]))
			elif i % roman_numeral[j] != 0 and i > roman_numeral[j]:
				print(j)
collect_number = int(input("Please enter your Number: "))
sorted_list = (get_standard_form(convert_to_list(collect_number)))
print(get_roman_numeral(sorted_list))
