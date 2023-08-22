#Britney Huiracocha
#Take-home test for Unit 2

#Task

#1. The total number of words
count = 0
with open('alice.txt') as book:
    for line in book:
        count += len(line.split())
print('Total number of words:', count)

#2. The average number of words in a line (total number of words / total number of lines)
lines = 0
with open('alice.txt') as book:
    for line in book:
        lines += 1
    numOfLines = lines
    avgNumWords = count/numOfLines
    
print('Average number of words in a line:', avgNumWords)

#3. The line with the most words and the number of words in that line
maxcount = 0
with open('alice.txt') as book:
    for line in book:
        count = len(line.split())
        if count>maxcount:
            maxline = line
            maxcount = count
print('Longest line has ', maxcount,' words: ',maxline)

#4. The total number of lines in your Python source code
lines = 0
with open('test2.py') as program:
    for line in program:
        lines += 1
    numOfLines = lines
    
print('Total number of lines in Python source code: ', numOfLines)

#5. Provide an interface that allows the user enter a word to look up how many lines contain that word and to see up to the first ten such lines.
# If no lines contain that word, then your program must output Not found.
response = input('Enter word: ')
count = 0
with open('alice.txt') as book:
    for line in book:
        if response in line:
            print(line)
            count+=1
            if count ==10:
                break      
    for line in book:
        if response in line:
            count+=1
    if count == 0:
        print('Not found')
    else:
        print(count,' lines contain ', response)
