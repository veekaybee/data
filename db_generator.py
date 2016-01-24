"""
Generates an n x 3 table of random data for testing small datasets
Asks user to input n value for row size
One column for float, one for int, one for text values
Exports results as pandas dataframe to csv file
"""

import random
import numpy as np
import pandas as pd
from string import ascii_lowercase


def numpy_random(n):
	"""Return a  random float"""
	return np.random.random(n)

def numpy_randint(n):
    """Return a random int."""
    return np.random.randint(0,100, size= n) 

def text_col(n):
	"""generates n random rows of lower-case strings of length 1 to 20"""
	letters = ascii_lowercase
	random_number = n
	random_letter = random.choice(letters)
	word_list = []

	for i in xrange(0,n):
		word = ''
		for number in xrange(0,random.randint(1,20)):
			word += random.choice(letters) 
			complete_word = word		
		word_list.append(complete_word)

	return word_list


def main():
	"""Asks user to input desired matrix row size, appends
	all values into numpy array, transposes array
	to correct shape,  and generates pandas dataframe 
	to output to csv 
	"""
	value = raw_input("How many rows do you want your matrix to have? : ")
	rows = int(value) + 1
	x, y, z = text_col(rows), numpy_random(rows), numpy_randint(rows)
	n = np.array([x, y,z])
	#transposes rows to columns based on input number of rows specified
	nx =np.transpose(n).reshape((rows,3))
	df = pd.DataFrame(nx,columns=['text_col','float_col','int_col'])
	df.to_csv("table.csv", sep=',')

if __name__ == '__main__':
	main()




		
