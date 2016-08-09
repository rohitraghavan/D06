import os

def list_files():
	os.chdir("/Users/rohitraghavan/Bootcamp/D05")
	print("Path: " + os.getcwd())
	print("Files are:", end=" ")
	for file_name in os.listdir():
		if file_name.endswith(".py"):
			print(file_name, end=", ")
	print("")

def main():
	list_files()

if __name__ == "__main__":
	main()