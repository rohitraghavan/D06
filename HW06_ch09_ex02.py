#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def count_no_e():
	total_word_count = 0
	words_without_e_count = 0
	words_without_e_list = list()
	with open("words.txt", "r") as words_file:
		words_list = words_file.readlines()
		for word in words_list:
			word = word.strip()
			total_word_count = total_word_count + 1
			if has_no_e(word):
				words_without_e_list.append(word)
				words_without_e_count = words_without_e_count + 1

	print_no_e(words_without_e_list, words_without_e_count, total_word_count)

def has_no_e(word):
	if "e" not in word:
		return True
	return False

def print_no_e(words_without_e_list, words_without_e_count, total_word_count):
	print("Words without 'e':")
	for word in words_without_e_list:
		print(word)
	words_without_e_percentage = (words_without_e_count / total_word_count) * 100
	print("The percentage of words without 'e' is: " + repr(words_without_e_percentage))

##############################################################################
def main():
    count_no_e()

if __name__ == '__main__':
    main()
