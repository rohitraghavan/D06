#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Cafe leaf
#       2: Coffee cola
#       3: Cool fella
##############################################################################
# Imports

# Body
def uses_only(word, allowed_letters):
	for word_letter in word:
		if word_letter not in allowed_letters:
			return False
	return True

def contains_only_allowed_letters(allowed_letters):
	with open("words.txt", "r") as words_file:
		words_list = words_file.readlines()
		for word in words_list:
			word = word.strip()
			if uses_only(word.lower(), allowed_letters):
				print(word)

##############################################################################
def main():
    contains_only_allowed_letters("acefhlo")


if __name__ == '__main__':
    main()
