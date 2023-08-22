#Britney Huiracocha
#Take-home test for Unit 5

#Task


def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789@_'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

import os
counts=[]
mentionedWords=[]
def findMentions(filename):
    with open(filename) as file:
        for word in cleanedup(line).split():
            if filename[0]=='@':
                if word in counts:
                    counts[word]+=1
                else:
                    counts[word]=1
                print(filename)
     
for word in counts:
    mentionedWords.append([counts[word],word])
 
 
for filename in os.listdir('.'):
    if filename[-3:]=='.tweets':
        findMentions(filename)
                 
mentionedWords.sort()
for word in counts:
    print (mentionedWords[3:])
