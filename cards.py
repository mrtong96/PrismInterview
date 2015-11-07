
import random

class Deck():
    suits = ['spades', 'diamonds', 'clubs', 'hearts']
    values = ['2', '3', '4', '5', '6', '7', '8', '9',
        '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = self.NewDeck()

    def NewDeck(self):
        cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                cards.append(Card(suit, value))
        return cards

    def Shuffle(self):
        self.cards = self.NewDeck()
        random.shuffle(self.cards)

    def GetNextCard(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise Exception('Error: no cards left in the deck')

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)

    def __repr__(self):
        return str(self)

def main():
    d = Deck()
    print 'initial dealing of deck:'
    cards = []
    for i in range(52):
        cards.append(d.GetNextCard())
    print str(cards)
    print


    print 'shuffled dealing of deck:'
    d.Shuffle()
    cards = []
    for i in range(52):
        cards.append(d.GetNextCard())
    print str(cards)
    print

    print 'The exception thrown when you try to deal from an empty deck:'
    try:
        d.GetNextCard()
    except Exception as e:
        print e
    print

    print 'sample from shuffling, dealing 5 cards, shuffling again, then dealing 5 more cards:'
    d.Shuffle()
    first_cards = []
    for i in range(5):
        first_cards.append(d.GetNextCard())
    d.Shuffle()
    second_cards = []
    for i in range(5):
        second_cards.append(d.GetNextCard())
    print str(first_cards)
    print str(second_cards)
    print

if __name__ == "__main__":
    main()