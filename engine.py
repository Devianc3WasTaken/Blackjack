from deck import Deck

def pointCalculation(card):
        if (card == 'J' or card == 'Q' or card == 'K'):
            return 10
        elif (card == 'A'):
            return 11
        else:
            return card


def gameEngine(currentPlayer, deckPosition):
    deck = Deck()

    totalPoints = 0
    currentCards = []
    hasAce = False
    dealtCards = 0

    while(totalPoints < 21):

        currentCards.append(deck.cards[deckPosition])
        totalPoints += pointCalculation(deck.cards[deckPosition])

        if(pointCalculation(deck.cards[deckPosition]) == 11):
            hasAce = True 

        deckPosition += 1
        dealtCards += 1

        if(totalPoints > 21):
            if(hasAce):
                totalPoints -= 10
                hasAce = False
            else:
                break

        if(dealtCards >= 2 and totalPoints < 21):
            print("You have a deck worth " , totalPoints)
            print("Your deck is: " , currentCards)
            print()
            print("[1] Hit")
            print("[2] Stand")
            userInput = input("Enter your choice: ")
            userInput = int(userInput)
            if (userInput == 2):
                dealtCards = 0
                break

    print("=========================")

    if(totalPoints == 21):
        print("BLACKJACK!")
    elif(totalPoints > 21):
        print("BUST!")
        
    print("Your total deck points is:" , totalPoints)
    print("Your deck is:" , currentCards)
    print("=========================")
    dealtCards = 0
    return totalPoints, deckPosition