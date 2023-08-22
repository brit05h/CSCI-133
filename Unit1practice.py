#Unit 1 - Apply what you know

#1.1
students = ['Fred','Ted','Ed']
for student in students:
    print('Hello', student)

#1.2
meats = ['ham', 'pastrami', 'roast beef', 'chicken']
breads = ['rye', 'whole wheat', 'a roll']
for meat in meats:
    for bread in breads:
        print(meat,'on', bread)

#1.3 Write a program that checks the word 'pineapple' and tells us what vowels it contains
vowels = 'aeiou'
word = 'pineapple'
for letter in vowels:
    if letter in word:
        print(letter, 'is in', word)

#2 Write a program that prints the letters in the alphabet, one per line.
alphabet = ['abcdefghijklmnopqrstuvwxyz']
for alph in alphabet:
    print(alph)

#3 The word ‘substantiate’ contains the word ‘ant’.  Write a program that reports which
# of the following words is contained in ‘substantiate’: ‘ate’, ‘state’, ‘a’, ‘substantiate’,
# ‘it’, ‘tan’
longword = 'substantiate'
words = ['ate','state','a','substantiate','it']
for word in words:
         if word in longword:
             print(word, ' is a substring of' ,longword)

#4 Write a program that prints the name Fred 100 times, one time per line.  Your
# program should be reasonably short and should not include a list containing more
# than ten items or a string containing more than ten characters.
for x in '-----------':
        print('Fred')

#5 Write a program that counts down from 10 to 1.
numbers = [10,9,8,7,6,5,4,3,2,1]
for number in numbers:
    print(number)

#6 Write a program that tells us which vowels are used in each of the following words:
# ‘apple’, ‘banana’, ‘peach’, ‘grapefruit’.
fruits = ['apple', 'banana','peach','grapefruit']
for fruit in fruits:
    print('Vowels in', fruit)
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel in fruit:
            print(vowel)

