# Integers
age = 22
count = 0
temperature = -5

#print(str(age))

# Floats (numbers with decimal)
price = 20.99
height = 5.0
new_temperature = 98.0

#addition
#print(8+3)
#subtration
#print(7-5)
#division
#print(3/5)
#multiplication
#print(3*5)
#remainder
#print(15 % 4)
#power
#print(2 ** 3)

# PEDMAS (Parentheses, Exponents, Multification, Division, Subtraction)
#result = 2 + 3 * 4
#print(result)

#result = (2 + 3) * 4
#print(result)

#x = 10

# x = x + 5
#x += 5
#print(x)

# x - x =3
#x -= 3
#print(x)

# x * x = 2
#x *= 2
#print(x)

# x / x = 4
#x /= 4
#print(x)

# Converting between types
#age_text = "22"
#age_number = int(age_text)
#print(age_number + 3)

#price_text = "20.99"
#price_number = float(price_text)
#print(price_number * 2)

#score =  98
#score_text = str(score)
#print("Your score is " + score_text)

# Sbsolute value (it removes neative sign)
#print(abs(-5))
#print(abs(3))

# Round numbers
#print(round(3.7))
#print(round(3.14159, 2))

numbers = [5, 2, 9, 3, 8, 7]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Won't work
user_age = input("Enter your age: ")
next_year = user_age + 1

# This works
age_text = input("What is your age?: ")
new_age = int(age_text)
next_year = new_age + 1
print("Next year you'll be " + str(next_year))

# Check if number are odd or even

number = 7
remainder = number % 2

print(remainder)
if remainder == 0:
   print(str(number) + " is even") 
else: 
   print(str(number) + " is odd")   



