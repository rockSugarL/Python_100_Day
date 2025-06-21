#Python 100-2
#day2.1 challenge
#print(type(39))
a = "39"
first_digit = int(a[0])
second_digit = int(a[1])
two_digit_number = second_digit + first_digit
print(two_digit_number)

#mathematical operations

#()
#* *
#* /
# + -

print(3*(3+3)/3-3)

# Day 2.2 BMI calculator excercise
# don't change the code below
eight = input ("enter your height in m:")
weight = input (" enter your weight in kg:")
# don't change the code above

# write your code below this line
BMI= weight / height**2
#print(type(height))

#bmi = int(weight) / float(height)**2
bmi_as_int = int (bmi)
print(bmi_as_int)
= input("enter your height in m:")
weight = input("enter your weight in kg:")

#weight_as_int = int(weight)
#height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#Day 2.end
rint(round(4/3))
print(type(7/3))

#Day 2.3 Life in weeks exercise
# don't change the code below
age = input ("what's your current age?")

# 1 year = 365 days = 52 weeks =12 months
# write your code below this line: 告诉我们实际上还剩下多少天，几周和几月？假如我们都活都90岁
your_age =int(age)
years = str(90-(your_age * 1))
days = str((90-your_age )* 365)
months = str((90-your_age )* 12)
print("you have "+years+"years"+","+days+"days"+","+months+"months"+"left")

#老师的做法：
message = f"you have{days}days,{months}months,{years}years"
print(message)

# Day2 project_Tip calculator
#welcome to the tip calculator
# what was the total bill? $124.56
#what percentage tip would you like to give ? 10,12,or 15?  12
# how many people to split the bill? 7
# each person should pay: $19.93

total_bill = input( "what was the total bill?:" )
tip_you_given= input ("what percentage tip would you like to give ? 10,12 or 15?:")
total_people = input ("how many people to split the bill? :")
#print(type(total_people))
bill = float(total_bill)
tips = int(tip_you_given)
people = int(total_people)

each_person_bill = (bill * (1+ tips / 100))/people

print(each_person_bill)

#老师的做法
print("welcome to the tip calculator!")
bill = float (input("what was the total"))
tip = float (input("how much tip would you like to give? 10,12 or,15?:"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round (bill_per_person)
print(f"Each person should pay ${final_amount}")