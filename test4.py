#Britney Huiracocha
#Take-home test for Unit 4

'''Task:
The game starts with certain initial amount of dollars.
At each round of the game, instead of flipping a coin, the player shuffles a deck and draws 6 cards. If the drawn hand contains at least one ace, the player gains a dollar, otherwise they lose a dollar.
The game runs until the player either runs out of money or doubles their initial amount.
'''

import cards

def oneGame(initial):
    countCards = 0
    bankroll = initial
    
    while 0 < bankroll < 2 * initial:
        numberofAces = 0
        d = cards.shuffledDeck()

        for num in range(6):
            card = d[num]
            if cards.faceValueOf(card) == 'ace':
                numberofAces += 1
                
        if numberofAces == 0:
            bankroll -= 1
        else:
            bankroll += 1

        countCards += 1

    return countCards

while True:
    initial = int((input('Enter initial amount:')))
    totalCards = 0

    for number in range(1000):
        totalCards += oneGame(initial)
    print('Average number of rounds:', totalCards/1000)
