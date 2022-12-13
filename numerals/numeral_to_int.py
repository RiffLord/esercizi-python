#!/usr/bin/env python3
'''
Legge una lista di numeri interi che rappresentano i numeri romani nel formato
XKCD di Randall Munroe, restituendo il valore effettivo del numero come intero
'''
def numeral_to_int(numerals : list[int]) -> int:
	result = 0
	for i in range(len(numerals)):
		if i < len(numerals) - 1 and numerals[i] < numerals[i + 1]:
			result += numerals[i] * (-1)
		else:
			result += numerals[i]
	return result
	pass

#==============================================================================#
if __name__ == '__main__':
	print(numeral_to_int([500, 100, 100, 100, 50, 10, 10, 10, 1, 10]))
	print(numeral_to_int([1, 10, 100, 1000]))
	print(numeral_to_int([100, 100, 100, 10, 100, 5, 1, 1]))
	print(numeral_to_int([100, 100, 100, 10, 100, 1, 10]))
	print(numeral_to_int([100, 100, 100, 10, 100, 5, 1, 1, 1]))
	print(numeral_to_int([100, 100, 100, 10, 100, 5, 1, 1]))
	print(numeral_to_int([100, 100, 100, 10, 100, 5, 1]))
	print(numeral_to_int([100, 100, 100, 10, 100, 5]))
	print(numeral_to_int([100, 100, 100, 10, 100, 1, 5]))
	print(numeral_to_int([10, 1, 10]))
	print(numeral_to_int([1, 1]))
	print(numeral_to_int([1, 5, 5]))

