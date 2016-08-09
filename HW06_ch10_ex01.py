# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_of_nos):
	sum_of_nos = 0
	for nos in list_of_nos:
		if type(nos) is list:
			sum_of_nos += nested_sum(nos)
		elif type(nos) is int or type(nos) is float:
			sum_of_nos += nos
	return sum_of_nos

def main():
	sum_of_nos = nested_sum([1, [2, [1, 2]], [3]])
	print ("Sum of the digits is: " + str(sum_of_nos))

if __name__ == "__main__":
	main()