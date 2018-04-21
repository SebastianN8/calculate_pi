#
# calculate_pi.py
#
# Created by: Sebastian N
# Created on: April 19
#
# This program calculates pi according to iterations
#

# This is where math.floor comes from
import math

# Function that contains the loop in order to get the result of a gregory leibniz series
def calculate_pi(iterations_passed_in):
	# Variables that will carry the count in the loop, the resul of the addition and the result for pi.
	the_iterations = 0
	addition = 0
	pi = 0

	# If statement that takes care of filtering inputs such as 0 and decimal numbers.
	if 	(iterations_passed_in == math.floor(iterations_passed_in)) and iterations_passed_in > 0: 
		for the_iterations in range (0, iterations_passed_in):
			the_iterations_float = float(the_iterations)
			addition = addition + math_calculation(the_iterations_float)
		pi = (math.floor((addition * 4)*1000))/1000
		print str(pi)

	else:
		print 'Invalid iterations'

# Function that does the math involved in the gregory leibniz addition to be looped in calculate_pi()
def math_calculation(exponent):
	numerator = ((-1)**exponent)
	denominator = numerator / ((2*exponent) + 1)
	return denominator

# Variable that saves the iteration that the user wants
iterations = input('What are the number of iterations that you need: ')

# Calling function
the_result = calculate_pi(iterations)
