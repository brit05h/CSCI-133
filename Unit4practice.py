#Unit 4 - Apply What you know
#0:

    #0.1 Write a module that contains the average and cleanedup functions.  Then use
    # these functions in a simple test program, importing them from the module.
import my
print(my.average([1,2,3,4]))
print(my.cleanedup('This--WOW--is ready for split()'))

''' 0.2 Write a program that runs simulations to find out how many $1 bets it takes on
average to either go broke or double your money, assuming that you start with
$10 and have an even chance of winning or losing any single bet.  Use a function
to simulate one game, returning the number of bets, and call the function many
times to determine the average.'''
import random
countFlips = 0
initial = 10
bankroll = initial
while 0 < bankroll < 2*initial:
    flip = random.choice(['heads', 'tails'])
    countFlips += 1
    if flip == 'heads':
        bankroll += 1
    else:
        bankroll -= 1
print(countFlips)

'''0.3. Modify the previous program so that it includes a function for running an
experiment in which an average is determined for any given set of starting
bankrolls and any given number of games.  Use the function to find the average
length of games starting with $10, $20 and $40, using 2,000 games of each kind.'''
import random
def oneGame(initial):
    countFlips = 0
    bankroll = initial
    while 0 < bankroll < 2*initial:
        flip = random.choice(['heads', 'tails'])
        countFlips += 1
        if flip == 'heads':
            bankroll += 1
        else:
            bankroll -= 1
    return countFlips
def experiment(initials, repetitions):
    for initial in initials:
        print('Initial bankroll:', initial)
        totalFlips = 0
        for number in range(repetitions):
            totalFlips += oneGame(initial)
        print('Average number of flips:', totalFlips/repetitions)
        print()
experiment([10, 20, 40], 2000)


'''0.4. Write a program that runs simulations to find out the chance that at least one
student in a class of 30 will get his or her own paper if the teacher hands them
out for grading at random.  Use a function to simulate passing back the papers
one time and another to run experiments by calling the first function repeatedly.'''
import random
def paperStatus(classSize):
    papers = list(range(classSize))
    random.shuffle(papers)
    for student in range(classSize):
        if papers[student] == student:
            return 'warning'
    return 'okay'
print(paperStatus(30))
print(paperStatus(30))
print(paperStatus(30))


# 1. Write a program that prints the name Fred 100 times, one time per line.
for number in range(100):
    print('Fred')

'''2. Write a program that produces word­scramble puzzles.  The program should choose
words at random from Pride and Prejudice, display the letters of the word in a
random order and challenge the user to guess the original word.'''

'''2.1 Start by writing a function called wordlist that takes a filename and compiles a
list of all the unique words found in the file.  For example, wordlist('pap.txt')
should return a list of the words in Pride and Prejudice.
In writing this function you will want to add strings to a list only if they are not
already in it.  The condition x not in y holds if x is not one of the items in the
collection called y.'''
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = []
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word not in words:
                    words.append(word)
    return words

words = wordlists('pap.txt')
print(words)
'''
    
2.2 In order to scramble a string, you’ll have to start by turning it into a list of
individual characters.  After the list is rearranged randomly, you’ll want to put the
characters back together into a single string.  Write a function called rejoin that
does this.  The call rejoin(['c', 'a', 't']) should return the string 'cat'.'''
import random

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = []
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word not in words:
                    words.append(word)
    return words

def rejoin(characters):
    word = ''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

s = scramble('cat')
print(s)

    
'''2.3 Write a function called scramble that takes in a string and returns a string with the
same letters in a random order.
Finally, use these three functions to write the puzzle program.'''
import random

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = []
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word not in words:
                    words.append(word)
    return words

def rejoin(characters):
    word = ''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlists('pap.txt')

while True:
    word = random.choice(words)
    mixed = scramble(word)
    print ('Letters:', mixed)
    guess = input('Guess: ')
    if guess == word:
        print('Right!')
    else:
        print('Sorry, the word was', word)


'''3. Most of the puzzles produced by the previous program are much too hard.  Modify
the program so that it gives the user a three­letter puzzle to start and then adjusts the
number of letters up by one every time a correct answer is given and down by one for
every wrong answer.  In this way, the program will generally produce puzzles that are
at the user’s level.
Rather than keeping all possible words in a single list, you should use a dictionary.  If
the dictionary is called wordlists, then wordlists[7] should be a list of all words in
Pride and Prejudice that are seven letters long.'''
import random

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = ()
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                length = len(word)
                if length in words:
                    words[length].append(word)
                else:
                    words[length] = [word]
    return words

def rejoin(characters):
    word = ''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlists('pap.txt')

level = 3

while True:
    word = random.choice(words[level])
    mixed = scramble(word)
    print ('Letters:', mixed)
    guess = input('Guess: ')
    if guess == word:
        print('Right!')
    else:
        print('Sorry, the word was', word)
        level -= 1



'''4. Write a program that randomly chooses a hand of five cards from a standard deck of
playing cards and displays it for the user to see.  Use a function that returns a shuffled
deck, ready for dealing.
A standard deck consists of 52 cards.  There are 13 each of four suits: clubs,
diamonds, hearts and spades.  Within each suit, the 13 face values are: ace, 2, 3, 4, 5,
6, 7, 8, 9, 10, jack, queen and king.  We identify a card by its face value and suit, e.g.
the 2 of hearts, the jack of clubs, etc.'''
import random

faceValues = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

suits = ['clubs','diamonds','hearts','spades']

def shuffledDeck(): 
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + 'of' + suit)
    random.shuffle(deck)
    return deck

d = shuffledDeck()

for number in range(5):
    print(d[number])
    
print(deck)

'''5. Modify the previous program so that, in addition to displaying a five­card hand, it
reports the number of aces and the number of clubs in the hand.  Use one function to
determine the face value, given a string like 'queen of diamonds', and another one to
determine the suit.'''
import random

faceValues = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

suits = ['clubs','diamonds','hearts','spades']

def shuffledDeck(): 
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + 'of' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]

def suitOf(card):
    return card.split()[2]

d = shuffledDeck()

numberOfAces = 0
numberOfClubs = 0
for number in range(5):
    card = d[number]
    print(card)
    if faceValueOf(card) == 'ace':
        numberOfAces += 1
    if suitOf(card) == 'clubs':
        numberOfClubs += 1

print('Number of aces:', numberOfAces)
print('Number of clubs:', numberOfClubs)

'''6. Collect the card­related functions you have written into a module called cards.py and
rewrite the previous program so that it begins by importing this module.'''
import cards

d = cards.shuffledDeck()

numberOfAces = 0
numberOfClubs = 0
for number in range(5):
    card = d[number]
    print(card)
    if cards.faceValueOf(card) == 'ace':
        numberOfAces += 1
    if cards.suitOf(card) == 'clubs':
        numberOfClubs += 1

print('Number of aces:', numberOfAces)
print('Number of clubs:', numberOfClubs)








