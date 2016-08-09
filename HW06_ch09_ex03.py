#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import sys
# Body
def avoids(word, forbidden_letters):
    """ return True if word NOT forbidden"""
    for forbidden_letter in forbidden_letters:
        if forbidden_letter in word:
            return False
    return True

def get_non_forbidden_words_cnt(forbidden_letters):
    words_wo_forbiddenltrs_count= 0
    with open("words.txt", "r") as words_file:
        words_list = words_file.readlines()
        for word in words_list:
            word = word.strip()
            if avoids(word, forbidden_letters):
                words_wo_forbiddenltrs_count = words_wo_forbiddenltrs_count + 1
    return words_wo_forbiddenltrs_count


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbidden_letters = input("Enter forbidden letters:")
    words_wo_forbiddenltrs_count = get_non_forbidden_words_cnt(forbidden_letters)
    print("The number of words with don't contain any of the forbidden letters are " + repr(words_wo_forbiddenltrs_count))


def forbidden_param():
    """ return count of words NOT forbidden by param"""
    if len(sys.argv) == 2:
        forbidden_letters = sys.argv[1]
        words_wo_forbiddenltrs_count = get_non_forbidden_words_cnt(forbidden_letters)
        print("The number of words with don't contain any of the forbidden letters are " + repr(words_wo_forbiddenltrs_count))
    else:
        print("Please enter one argument with forbidden letters")


# Incomplete; not working yet!
def find_five():
    max_non_forbidden_words_cnt = 0
    for ltr1 in range(97, 123):
        for ltr2 in range(98, 123):
            for ltr3 in range(99, 123):
                for ltr4 in range(100, 123):
                    for ltr5 in range(101, 123):
                        non_forbidden_words_cnt = get_non_forbidden_words_cnt(chr(ltr1)+chr(ltr2)+chr(ltr3)+chr(ltr4)+chr(ltr5))
                        if non_forbidden_words_cnt > max_non_forbidden_words_cnt:
                            max_non_forbidden_words_cnt = non_forbidden_words_cnt
    print("Number of words excluded is " + str(max_non_forbidden_words_cnt))


##############################################################################
def main():
    ...
    # Your final submission should only call five_five
    find_five()

if __name__ == '__main__':
    main()
