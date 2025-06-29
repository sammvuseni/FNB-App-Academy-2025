# Loops let you repeat code without writing it multiple times
for i in range(1, 6):
   print("Hello " + str(i))

# Count from o to 5   
for i in range(6):
   print(i)
 
 # Steps  
for i in range(0, 11, 4):
   print(i)
   
# Countdown
for i in range(10, 0, -1):
   print(i)
print("Blast off!")

# Print loop number 5 in one line
for i in range(5):
   print(i, end=" ")
   
# Loops each charecter in a string

print("\n")
word = "Python"
for letter in word:
   print(letter)
   
# Loop into list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
   print("I like " + fruit)
   
# While loop
count = 1
while count <= 5:
   print("Count: " + str(count))
   count += 1
   
password = ""
while password != "cheese":
   password = input("Enter password: ")
   if password is not "cheese":
      print("Wrong password, try again")
print("Welcome!")


   
   
   
   
