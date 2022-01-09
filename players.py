def players():
    print("How many players would you like?")
    amountOfPlayers = input("Please enter a value of 1 to 4: ")
    amountOfPlayers = int(amountOfPlayers)
    print(amountOfPlayers)

    if (amountOfPlayers < 1 or amountOfPlayers > 4 ):
        print("Invalid number of players!")
        print("Exiting program")
        quit()

    return amountOfPlayers