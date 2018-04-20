#
# calculate_pi.py
#
# Created by: Sebastian N
# Created on: April 19
#
# This program calculates pi according to iterations
#

# Function
def calculating_pi():
	# Variables
	iterations_input = int(input('Iterations needed: '))
	initial = 0
	addition = 0
	pi = 0

	# Loop
	while (initial is not iterations_input):
		addition = (addition) + (((-1)**initial)/((2*initial) + 1))
		initial = initial + 1
	pi = addition * 4

	return pi 


# Call function
the_result = calculating_pi()
print str(the_result)