#
# calculate_pi.py
#
# Created by: Sebastian N
# Created on: April 19
#
# This program calculates pi according to iterations
#
import math

# Function
def calculate_pi(iterations_passed_in):
	# Variables
	the_iterations = 0
	addition = 0
	pi = 0

	# Loop
	if 	(iterations_passed_in == math.floor(iterations_passed_in)) and iterations_passed_in > 0: 
		for the_iterations in range (0, iterations_passed_in):
			the_iterations_float = float(the_iterations)
			addition = addition + math_calculation(the_iterations_float)
		pi = (math.floor((addition * 4)*1000))/1000
		print str(pi)

	else:
		print 'Invalid iterations'


def math_calculation(exponent):
	numerator = ((-1)**exponent)
	denominator = numerator / ((2*exponent) + 1)
	return denominator

# Variables
iterations = input('What are the number of iterations that you need: ')

# Calling function
the_result = calculate_pi(iterations)
