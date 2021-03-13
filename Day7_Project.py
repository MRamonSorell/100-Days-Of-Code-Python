# M R Sorell
# Project 7 - Hangman
# Flow Chart Programming

# start generate a random word
# generate blanks for each letter in the word
# guess a letter
# is the letter in the word (yes or no)
# yes replace blank with letter
# yes are all the blanks filled
# if no
# guess again
# repeat until blanks are gone or no more guesses allowed

# picking random words

import random

word_list = ["ardvark", "baboon", "camelcase", "baseball", "honeycomb", "airbnbhotel", "phonecard"]

word_choice = random.choice(word_list)

print(word_choice)

word_length = len(word_choice)

game_word = []

for blank in word_choice:
    game_word.append('_')

while ('_' in game_word):
    guess = input("Guess a letter: ").lower()

    hangmanWord = list(word_choice)

    for item in range(word_length):
        letter_hold = hangmanWord[item]
        if guess == letter_hold:
            game_word[item] = guess


    print(game_word)

print("Game won!")