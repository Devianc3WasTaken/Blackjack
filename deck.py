import random

class Deck:
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A',
                        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
                        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
                        2,3,4,5,6,7,8,9,10,'J','Q','K','A']

        random.shuffle(self.cards)