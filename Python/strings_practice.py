my_name = "Sam Buthelezi"
my_age = 45
my_city = "Dublin"

print("About Me:")
print(my_name)
print("I am " + str(my_age) + " years old")
print("I live in " + my_city)

print("My name has " + str(len(my_name)) + " characters")

# Joining strings together 
first_name = "Mvuseni"
last_name = "Buthelezi"
full_name = first_name + " " + last_name
print(full_name)

# Adding to existing strings
message = "Hellow"
message += " World"
message += " !"
print(message)

# Repeating strings
laugh = "Ha" * 5
print(laugh)

# Useful string methods
text = "Hello World"

print(text.upper()) #string converted to uppercase
print(text.lower()) #string converted to lowercase
print(text.title()) #each word to be titlecased
print(text.capitalize()) #first letter to be uppercase the rest lowercase

# Removing extra spaces
messy_text = "       Hi stranger     "
print(messy_text.strip()) #use .strip to remove extra spaces

# Finding text
sentence = "Sawubona Ntokazi enhle!"

print(sentence.find("enhle")) #it will give a letter number in a sentence
print(sentence.find("Themba")) #it will show "-1" number as the word is not found
print(sentence.count("o")) #count how many time we have letter "o" on a sentence

# Checking what is in text
text = "Hellow123"
print(text.startswith("Hellow")) #respond will be true if available and false if not
print(text.endswith("123"))
print("Python" in sentence)

# Replacing a text
message = "I love javaScript"
new_message = message.replace( "javaScript", "Python")
print(new_message)

# Splitting text
sentence = "apple, banana, cherry"
fruits = sentence.split(",")
print(fruits)

words = "Hellow World Python".split()
print(words)

letters = ['a', 'b', 'c', 'd','e'] #list back to a string
new_word = "".join(letters)
print(new_word)

#String slicing(Getting a part of a string)
text = "Python Programming"
print(text[0:6])
print(text[7:18])
