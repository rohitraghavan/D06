import random

def write_random_numbers():
	random_no_file = open("random_numbers.txt", "w")
	for count in range(0, 10):
		random_no = random.randint(1, 1000)
		random_no_file.write(repr(random_no) + " " )
	random_no_file.close()

def main():
	write_random_numbers()

if __name__ == "__main__":
	main()