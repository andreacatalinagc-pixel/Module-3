# TODO: Create a string variable with a sentence
sentence = "Learning Python is fun"
print(sentence)

# TODO: Convert the string to uppercase
upper_sentence = sentence.upper()
print(upper_sentence)
# TODO: Convert the string to lowercase
lower_sentence = sentence.lower()
print(lower_sentence)
# TODO: Capitalize the first letter of each word
title_sentence = sentence.title()
print(title_sentence)

# TODO: Replace a word in the string
replaced_sentence = sentence.replace("fun", "interesting")
print(replaced_sentence)

# TODO: Split the string into a list of words
words_list = sentence.split()
print(words_list)

# TODO: Join the list of words back into a string using a different separator
joined_sentence = "-".join(words_list)
# TODO: Find the position of a specific word in the string
position = sentence.find("Python")

# TODO: Check if the string starts with a specific word
starts_with_learning = sentence.strip().startswith("Learning")
print(starts_with_learning)
print("Starts with 'learning':", starts_with_learning)

# TODO: Remove leading and trailing whitespace from a string
trimmed_sentence = sentence.strip()
print(trimmed_sentence)
print("Trimmed sentence:", trimmed_sentence)

# Print the results of each operation

#3
# TODO: Create a list of numbers
numbers = [2, 4, 6, 8]

# TODO: Use a for loop to print each number in the list
for num in numbers:
    print("Number:", num)

# TODO: Use a for loop with enumerate() to print both index and value
fruits = ["apple", "banana", "cheffy"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
   
for index, value in enumerate(numbers):
    #print(index, value)
    if index % 2 == 0:
        print(f"{index}: {value}")

# TODO: Create a dictionary and use a for loop to print all keys and values
sara = {
    "name": "Sarah",
    "age": 23,
    "city": "Paris",
    "hobbies": ["reading", "swimming"],
    }
if sara["age"] >= 18:
    print("est majeur")
    print("est mineur")
# TODO: Use a for loop with range() to print numbers from 1 to 10
for key, value in sara.items():
        print(f"sarah{key}] = {value}")

# TODO: Use list comprehension to create a new list of squares of numbers

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)

range_example = [0, 1]
eleves = ["Alice", "Bob", "Charlie"]

for i in range_example: 
    for eleve in eleves:
        print(eleve)

range_example3 = range(3)
print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in range(1,11):
    print(x)
  
#IF
