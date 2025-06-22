# random module   module就像各个做汽车部件的人

import random

randomIntegeter = random.randint(1,10)
print(randomIntegeter)

randomFloat = random.random()*5
print(randomFloat)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

# Day 4.1 Heads or Tails Exercise

import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

import random
# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get the total number of items in list.
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
print(random_choice)

# IndexErrors and working with Nested Lists

# day 4.3 treasure map

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")