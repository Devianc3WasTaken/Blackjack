from engine import *
from players import players
#import deck

def main():
    deckPosition = 0
    amountOfPlayers = players()
    playerPoints = [None] * amountOfPlayers

    for currentPlayer in range(amountOfPlayers):
        print()
        print()
        print("#######################")
        print("You are player ", currentPlayer+1)
        print("#######################")
        print()
        
        playerPoints[currentPlayer], deckPosition = gameEngine(currentPlayer, deckPosition)
    
    print("Overall player points:", playerPoints)

#deck = Deck()
main()