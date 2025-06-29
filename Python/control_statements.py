# If & Else statements
from operator import not_


age = 18
if age >= 18:
   print("You are old enough.")
   print("You can vote")

print("This always prints")

temperature = 75
if temperature > 70:
   print("It's warm outside")
   
score = 95
if score >= 90:
   print("Excelent grade")

name = "John"
if name == "John":
   print("Hello, John!")
   
new_age = 16
if new_age >= 18:
   print("You can vote")
else:
   print("You cannot vote yet")
   
# Else If statement(elif in Python)  
score = 85
if score >= 90:
   print("Grade: A")
elif score >= 80:
   print("Grade: B")
elif score >= 70:
   print("Grade: C")
elif score >= 60:
   print("Grade: D")
else:
   print("Grade: F")
   
# Logical Operators(Combining conditions with And or Not)
age = 20
has_license = True

if age >= 18 and has_license:
   print("You can drive")
   
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
   print("No work today!")
   
is_raining = False

if not is_raining:
   print("Good day for a walk")
   
# Nested If Statement
weather = "sunny"
temperature = 75

if weather == "sunny":
   print("It is sunny")
   if temperature > 70:
      print("Perfecy weather for the beach!")
   else:
      print("Sunny but a bit too cool")
else:
   print("Not sunny today")
   
user_input = "yes"

if user_input == "yes" or user_input == "y" or user_input == "YES":
   print("you said yes")
   
if user_input.lower() == "yes" or user_input == "y":
   print("you said yes")
   
# The range checker
age_range = 25

if age_range >= 13 and age_range <= 19:
   print("You are a teenager!")
   
if 13 >= age_range <= 19:
   print("You are a teenager!")
   
# Validation Checker
email = "user@example.com"

if "@" in email and "." in email:
   email = "sammvuseni@gmail.com"
   print("Email looks valid")
else:
   print("Email doesn't look valid")
   
    
   
   
   
