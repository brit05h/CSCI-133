#Unit 5 - Apply what you know


# 0.1. Write a program that lists all items in the current directory.  Modify the program
# so that it lists all items in the parent of the current directory.
import os
path = '..'
for filename in os.listdir(path):
 print(filename)

# 0.2. Write a program that lists all items in the parent of the current directory, flagging
# directories in the listing with stars.
import os
path = '..'
for filename in os.listdir(path):
    newpath = os.path.join(path, filename)
    if os.path.isdir(newpath):
        print('***', filename)
    else:
        print(filename)

# 0.3. Modify the previous program so that the listing code is contained in a function
# called lister that takes a path and lists items in the location specified by the path,
# flagging directories with stars.  Call lister with both the path to the current
# directory and the path to its parent.
import os
def lister(path):
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            print('***', filename)
        else:
            print(filename)
lister('.')
print('---')
lister('..')

# 0.4. Modify lister so that it not only flags directories with stars but also lists their
# contents.
import os
def lister(path):
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            print('***', filename)
            lister(newpath)
        else:
            print(filename)
lister('..')

# 0.5. Modify lister again, so that subdirectory listings are indented appropriately.
import os
def lister(path, indent):
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            print(indent, '***', filename)
            lister(newpath, indent+' ')
        else:
            print(indent, filename)
parentOfParent = os.path.join('..', '..')
lister(parentOfParent, '')

# 0.6. Modify lister again so that only directories and Python program files are
# included in the listing.
import os
def lister(path, indent):
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename[len(filename)-1])
        if os.path.isdir(newpath):
            print(indent, '***', filename[len(filename)-1])
            lister(newpath, indent+' ')
        else:
            print(indent, filename[len(filename)-1])
parentOfParent = os.path.join('..', '..')
lister(parentOfParent, '')

# 1 write a program that prints Fred 100 times without using for or while
def printFred(times):
    print('Fred')
    if times-1 > 0:
        printFred(times-1)
printFred(100)

# 2 Write a program that lists all files in the current directory that contain the string 'random'.
import os

def contains(filename, pattern):
    with open(filename) as file:
        for line in file:
            if pattern in line:
                return True
    return False

for filename in os.listdir('.'):
    if contains(filename, 'random'):
        print(filename, 'contains random')


# 3 Write a program that reports the total number of files in the current directory and any
# subdirectories, subsubdirectories and so on.
import os

def counter(path):
    count = 0
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            count += counter(newpath)
            count += 1
        else:
            count += 1
    return count

print(counter('.'))

# 4 write a program that solves the word-scramble puzzles produced by program 2 in unit 4
import my

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return my.rejoin(letters)

print(alphabetize('race'))

unscramble = {}
with open('pap.txt') as book:
    with line in book:
        for word in my.cleanedup(line).split():
            key = alphabetize(word)

# 5 Write a program to find the five most common words in Pride and Prejudice ending with 'ing'
import my

counts = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

ingWords = []

for word in counts:
    if word[-3:] == 'ing':
        ingWords.append([counts[word],word])

ingWords.sort()
print(ingWords[-5:])

# 6 Write a program to choose a random five­card hand from a standard deck and then
# report if it is a one­ pair hand, a two­pair hand, a three­ of­ a ­kind hand or a four­ of ­a ­kind hand
import cards

def evaluate(hand):
    fvCounts = {}
    for card in hand:
        fv = cards.faceValueOf(card)
        if fv in fvCounts:
            fvCounts[fv] += 1
        else:
            fvCounts[fv] = 1
    justCounts = []
    for fv in fvCounts:
        justCounts.append(fvCounts[fv])
    justCounts.sort()
    if justCounts == [1,1,1,2]:
        return 'one pair'
    if justCounts == [1,2,2]:
        return 'two pair'
    if justCounts == [1,1,3]:
        return 'three of a kind'
    if justCounts == [2,3]:
        return 'full house'
    if justCounts == [1,4]:
        return 'four of a kind'
    return 'nothing'

hand = cards.shuffledDeck()[:5]
print(hand)
print(evaluate(hand))


