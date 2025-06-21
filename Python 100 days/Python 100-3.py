#Python 100-3

#条件语句
# if condition:
#   do this
# elso:
#   do this

print("welcome to the rollercoaster!")
height = int (input ("what is your height in cm ?"))

if height > 120:
   print("you can ride the rollercoaster!")
else:
    print("sorry, you have to grow taller before you can ride.")

# Day3.1 odd or even excercise
# don't change the code below
number = int(input("which number do you want to check"))
# don't change the code above
# write your code below thi line
# this is an odd number. 94;this is an even number. eg. when you hit run, this is what should happen;

if number % 2 == 0:
    print("this is a even number.")
else:
    print("this is an odd numer.")

# Nested if/else
# if condition:
#   if another condition:
    # do this
#   else:
    # do this
# else:
#    do this

#if/elif/else
# if contion1：
    # do A
# elif condition 2:
#    do B
# else:
    # do this
  
# day3.2 BMI 2.0 exercise
# don't change the code below;
height = float(input("enter your height in m:"))
weight = float (input("enter your weight in kg:"))
# don't change the code above

# writ your code below this line:

bmi = round (weight / height**2)

if bmi < 18.5:
    print(f"your bmi is {bmi},you are under weight.")
elif bmi < 25:
    print(f"your bmi is {bmi},you are a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi},you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi},you are obese.")
else:
    print(f"your bmi is {bmi},you are clinically obese")

# day 3.3 leap year exercise
year = int(input("which year do you want to check"))

# write your code below this line

if year %4 ==0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")

# day3.4 Pizza order exercise
print ("welcome to Python Pizza Deliveries!")
size = input ("what size pizza do you want?S,M,or L")
add_pepperoni = input("Do you want pepperoni?Y or N")
extra_cheese = input ("do you want extra cheese ? Y or N")

# write your code below this line
bill = 0
if size =="S":
    bill += 15
elif size =="M":
    bill += 15
elif size == "L":
    bill += 20
if add_pepperoni =="Y":
        if size =="S":
            bill += 2
        else:
            bill += 3
if extra_cheese =="Y":
    bill +=1
print(f"your final bill is ${bill}")

#logical operators
#  A and B  both have to true
#  C or D  just one of them is true==all have to be false
#  not E 扭转假的--》真的

#  day 3.5 love calculator exercise
print("welcome to the love Calculator!")
name1 = input("what is your name?\n")
name2 = input("what is your name?\n")

# write your code below this line 老师的做法
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("t")
o =lower_case_string.count("o")
v= lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e
love_score = int(str(true) + str(love))
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40 ) or (love_score <= 50):
    print(f"your love score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")

# day 3 project_Treasure Island 

print("Welcome to Treasure Island")
print("your mission is to find the treasire")
choice1 = input("you're at a crossroad, where do you want to go? type 'left'or 'right'.")

if choice1 == "left":
    choice2 = input('you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim"to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 =="red":
         print("It's a room full of fire. Game over.")
        elif choice3 =="yellow":
         print("You found the treasure! You Win!")
        elif choice3 == "blue":
         print("You enter a room of beasts. Game over.")
        else:
         print("You chose a door that doesn't exist. Game over")
    else:
      print("You got attacked by an angry trout. Game over.")
else:
  print("You fell into a hole.Game over.")