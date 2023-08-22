#Britney Huiracocha
#Take-home test for Unit 3

#Task

def cleanedup(s):
    letterssymbol = 'abcdefghijklmnopqrstuvwxyz@'
    cleantext = ''
    for character in s.lower():
        if character in letterssymbol:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

#1. The total number of tweets
numoftweets = 0
with open('elon-musk.txt') as book:
    for line in book:
        numoftweets += 1
print('Number of tweets:', numoftweets)

#2. The tweet that contains the most words (don’t use cleanedup for preprocessing here)
maxcount = 0
with open('elon-musk.txt') as book:
    for line in book:
        numofwords = len(line.split())
        if numofwords > maxcount:
            maxcount = numofwords
            maxline = line
    print('Tweet with max number of words:', maxline)

'''3. Finally, a username is a word that starts with an @ symbol (for example,
    @MarkTwain). For simplicity, we will assume that any word that contains @ at any position
    is a username (that is, consider Mark@Twain or @Mark@Twain@ to be valid usernames). Your
    program should compile the information on how many times different usernames are mentioned
    in Elon Musk’s tweets, then provide an interface that allows a user to quickly look up how
    many times any particular username is mentioned.'''

occurrences = {}
with open('elon-musk.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            if '@' in word:
                if word in occurrences:
                    occurrences[word] += 1
                else:
                    occurrences[word] = 1

while True:
    word = input('Enter username: ')
    if word in occurrences:
        print('Mentioned', occurrences[word], 'times.')
    else:
        print('Not mentioned.')
