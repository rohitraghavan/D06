#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, required_letters):
	for letter in required_letters:
		if letter not in word:
			return False
	return True

def contains_all_required_letters(required_letters):
	required_letters_words_count = 0
	with open("words.txt", "r") as words_file:
		words_list = words_file.readlines()
		for word in words_list:
			word = word.strip()
			if uses_all(word, required_letters):
				print(word)
				required_letters_words_count += 1
	print("There are {} words containing all letters in '{}'".format(required_letters_words_count, required_letters))

##############################################################################
def main():
    contains_all_required_letters("aeiou")
    contains_all_required_letters("aeiouy")


if __name__ == '__main__':
    main()
