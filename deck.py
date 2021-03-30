from card import Card
import random

class Deck:
    def __init__(self, value_start = None, value_end = None, number_of_suits = None):
        self.deck = []
        if (value_start == None) and (value_end == None) and (number_of_suits == None):
            self.deck = self.deck
        else:
            self.size = 0
            values = []
            i = value_start

            while i <= value_end:
                values.append(i)
                i += 1

            i = 0

            while i < number_of_suits:
                for value in values:
                    newCard = Card(Card.face_range[value - 1], Card.suit_range[(i % 4) - 1])
                    self.deck.append(newCard)
                    self.size += 1
                i += 1

    def __str__(self):
        if self.deck == []:
            return '[_]'
        else:
            return ','.join([item.get_face() + item.get_suit() + ":" + item.get_color()
                               for item in self.deck])

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

    def __repr__(self):
        return self.__str__()

    def column_print(self, column_len = 8):
        for index, card in enumerate(self.deck):
            if index % column_len == 0:  # at final column so print a carriage return
                print()
            print('{:}'.format(card), end='')
        print()
        print()


    def get_top_card(self):
        if len(self.deck) != 0:
            return self.deck[-1]
        else:
            return None

    def is_empty(self):
        if self.deck == []:
            return True
        else:
            return False

    def shuffle(self):
        random.shuffle(self.deck,random.random)

    def add_card(self, card):
        self.deck.append(card)

    def draw_card(self):
        if len(self.deck) != 0:
            return self.deck.pop()
        else:
            return None




def main():
    test_deck = Deck(1,13,10)
    test_deck.column_print()



if __name__ == "__main__":
    main()