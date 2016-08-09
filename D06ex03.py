def count_names():
	names_with_e_count = 0
	names_with_e_list = list()
	with open("roster.txt", "r") as names_file:
		names_list = names_file.readlines()
		for name in names_list:
			first_name = name.split()[0]
			if "e" in first_name:
				names_with_e_list.append(first_name)
				names_with_e_count = names_with_e_count + 1
	
	print_names(names_with_e_list, names_with_e_count)

def print_names(names_with_e_list, names_with_e_count):
	print("{} names contain the letter 'e'.".format(str(names_with_e_count)))
	print("The names are:")
	for name in names_with_e_list:
		print(name)

def main():
	count_names()

if __name__ == "__main__":
	main()