# loop

fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)

# day 5.1 avarage height exercise
student_heights = input("input a list of student heights").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int (student_heights[n])
print(student_heights)

# write your code:
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height/ number_of_students)

# for loop and rang function
# for number in range(a,b):
# print(number)
total = 0
for number in range (1,11):
    total += number
print(total)

# day 5.3 adding events
total = 0
for number in range (2,101,2):
    total += number
print(total)

total2 =0
for mubner in range(1,101):
    if number% 2 ==0:
        total2 += number
print(total2)

# day5.4 fizz buzz
for number in range(1,101):
    if number % 3 ==0 and number % 5 == 0 :
     print("fizzbuzz")
    elif number % 3 == 0:
     print("Fizz")
    elif number % 5 == 0 :
       print("buzz")
print(number)

# day 5 project _ create a password genertagor

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
