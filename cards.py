import random

def makeDeck():
    cardfaces = []
    suits = ["hearts", "diamonds", "clubs", "spades"]
    royals = ["jack", "queen", "king", "ace"]
    deck = []
    globals().update(locals())

    #now, let's start using loops to add our content:
    for i in range(2,11):
        cardfaces.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        cardfaces.append(royals[j])
    for k in range(4):
        for l in range(13):
            card = (cardfaces[l] + "_of_" + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
    #now let's shuffle our deck!
    random.shuffle(deck)

makeDeck()

def randomChoice():
    return deck.pop(0)
