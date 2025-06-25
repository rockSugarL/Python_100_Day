word_list = ["ardvark","baboon","camel"]

import random

chosen_word = random.choice(word_list)
guess = input("Guess a letter:").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

# challenge 2
# testing code
print(f'pssst,the solution is {chosen_word}.')
display = ["ardvark","baboon","camel"]
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter:").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)

# challenge 3

end_of_game = False

while not end_of_game:
    guess = input("guess a letter:").lower()

for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position:{position}\n Current:{letter}\n Guessed letter:{guess}")
    if letter == guess:
        display[position]=letter
print(display)

if "_" not in display:
    end_of_game = True
    print("You Win.")

# challenge 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

from replit import clear
import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
      print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])