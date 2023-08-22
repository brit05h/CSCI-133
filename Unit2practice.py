#Unit 2 - Apply What you know


#0:
''' #0.1  List the lines in the file pap.txt that contain the word ‘property’.
with open('pap.txt') as book:
    for line in book:
        if 'property' in line:
            print(line)
    #0.2 Count the number of words in the file pap.txt.
count = 0
with open('pap.txt') as book:
    for line in book:
        count += len(line.split())
print('Word count:', count)
    #0.3 Count the number of times the word ‘the’ appears in the file pap.txt.
count = 0
with open('pap.txt') as book:
    for line in book:
        for word in line.split():
            if word == 'the':
                count += 1
print("Number of times 'the' is used:", count)
    #0.4 Find and display the line in the file pap.txt containing the most words.
maxcount = 0
with open('pap.txt') as book:
    for line in book:
        count = len(line.split())
        if count>maxcount:
            maxline = line
            maxcount = count
print(maxline)'''

#1: Write a program that counts the number of times the lowercase letter ‘e’ is used in the
# file pap.txt.
count = 0
with open('pap.txt') as book:
    for line in book:
        for letter in line:
            if letter == 'e':
                count += 1
print("Number of times 'e' is used:", count)

#2:Write a program that checks itself and reports the number of lines of the program that
# contain the word ‘for’, either alone or as part of another word.
count = 0
with open('Unit2practice.py') as program:
    for line in program:
        if 'for' in line:
            count+= 1
print("Number of lines that contain 'for':", count)

#3:Write a program to determine which word is the shortest of the following: apple,
# banana, peach, plum, grapefruit.
words = ['apple', 'banana', 'peach', 'plum', 'grapefruit']
shortestLength = 999
for word in words:
    if len(word) < shortestLength:
        minWord = word
        shortestLength = len(word)
print('The shortest word is ', minWord)

#4: Write a program to determine the average of the numbers given in a list.  The first
# line of your program should give a name to a list of numbers to be averaged: e.g.
# numbers = [3, 17, 1, 44, 239].
numbers = [3, 17, 1, 44, 239]
total = 0
for number in numbers:
    total += number
print(total/len(numbers))

'''5: The list method append changes a list by adding an item at the end.  For example if
students refers to the list ['Ed' 'Ted', 'Fred'], then after calling
students.append('Jennifer') the list will be ['Ed' 'Ted', 'Fred', 'Jennifer'].  Write a
program using this method to print a list of the lengths of the words given in a list.
The first line of your program should give a name to the list of words, e.g. students =
['Ed', 'Ted', 'Fred', 'Jennifer'].  For this example, the output would be [2, 3, 4, 8].'''
students = ['Ed', 'Ted', 'Fred', 'Jennifer']

lengths = []
for student in students:
    lengths.append(len(student))
print(lengths)

'''6:The built­in function input displays a string on the screen and returns a string
containing what the user types in response.  For example, the statement answer =
input('How are you feeling? ') will display the given question and wait for the user to
type something and press enter.  Then answer will be assigned to a string that holds
what the user has typed.  Write a program using input that asks the user to type in any
number of words and then reports the maximum number of vowels contained in a
single word, e.g. ‘please’ is a six­letter word containing three vowels.'''
response = input('Please enter words: ')
words = response.split()

vowels = 'aeiou'
maxVowels = 0

for word in words:
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    if count > maxVowels:
        maxVowels = count
        maxWord = word

print(maxWord, maxVowels)


