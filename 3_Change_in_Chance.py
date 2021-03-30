###################################
# Assignment 3
###################################

from deck import Deck
import random
import numpy as np
import matplotlib.pyplot as plt

# set seed to reproduce the random draw result
random.seed(1005)

'''
3.1 Test the pair and flush
'''

# Function to check whether there is a pair in a hand
def is_pair(hand_list):
    '''
    Test whether there is a pair in the hand.
    :param hand_list: A hand draw from a random shuffled deck
    :return: True is there is a pair; False none of cards are pair.
    '''
    face_list = []
    for i in range(5):
        face_list.append(hand_list[i].get_face_index())
    # if
    if len(set(face_list)) < 5:
        return True
    else:
        return False


def is_flush(hand_list):
    '''
     Test whether there is a flush in the hand.
     :param hand_list: A hand draw from a random shuffled deck
     :return: True is there is a flush; False otherwise.
     '''
    suit_list = []
    for i in range(5):
        suit_list.append(hand_list[i].get_suit_index())

    if len(set(suit_list)) == 1:
        return True
    else:
        return False

'''
3.2 Repeated trails
'''
def change_pair_test(n_suits = 4, pairTest_size = 1000):
    '''
    :param n_suits: number of suits in the deck of cards
    :param pairTest_size: number of random draw of hands of cards
    :return: the frequency of pair occurrence
    '''
    change_pairTest_result = []
    for p in range(pairTest_size):
        the_deck = Deck(1, 13, n_suits)
        the_deck.shuffle()
        hand_list = []
        for i in range(5):
            hand_list.append(the_deck[i])

        newValue = is_pair(hand_list)
        change_pairTest_result.append(newValue)
    change_pair_rate = sum(change_pairTest_result) / pairTest_size
    return [change_pair_rate, change_pairTest_result]


def change_flush_test(n_suits = 4, flushTest_size = 1000):
    '''
      :param n_suits: number of suits in the deck of cards
      :param pairTest_size: number of random draw of hands of cards
      :return: the frequency of flush occurrence
      '''
    change_flushTest_result = []
    for p in range(flushTest_size):
        the_deck = Deck(1, 13, n_suits)
        the_deck.shuffle()
        hand_list = []
        for i in range(5):
            hand_list.append(the_deck[i])
        newValue = is_flush(hand_list)
        change_flushTest_result.append(newValue)
    change_flush_rate = sum(change_flushTest_result) / flushTest_size

    return [change_flush_rate, change_flushTest_result]



def main():
    # conduct change_pair_test varying number of suits from 1 to 10
    pair_change = []
    pairTest_data = []
    for i in range(10):
        newValue = change_pair_test(n_suits=i + 1, pairTest_size=1000)[0]
        newData = change_pair_test(n_suits=i + 1, pairTest_size=1000)[1]
        pair_change.append(newValue)
        pairTest_data.append(newData)
    print(pair_change)

    ##################
    # Print the data
    # ################

    # print_pair_data = [[], ] * 10
    # for j in range(10):
    #     print_pair_data[j] = np.transpose(pairTest_data[j])
    #     print(print_pair_data[j])

    # conduct change_flush_test varying number of suits from 1 to 10
    flush_change = []
    flushTest_data = []
    for i in range(10):
        newValue = change_flush_test(n_suits=i + 1, flushTest_size=1000)[0]
        newData = change_flush_test(n_suits=i + 1, flushTest_size=1000)[1]
        flush_change.append(newValue)
        flushTest_data.append(newData)
    print(flush_change)

    ##################
    # Print the data
    # ################

    # print_flush_data = [[], ] * 10
    # for j in range(10):
    #     print_flush_data[j] = np.transpose(flushTest_data[j])
    #     print(print_flush_data[j])

    ##################
    # Plot the result
    # ################

    # data to plot
    n_groups = 10
    pair = pair_change
    flush = flush_change

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    pair_bar = plt.bar(index, pair, bar_width,
                          alpha=opacity,
                       color='b', label='Pair')

    flush_bar = plt.bar(index + bar_width, flush, bar_width,
                          alpha=opacity,
                        color='g', label='Flush')

    plt.xlabel('Number of Suits')
    plt.ylabel('Success Rate')
    plt.title('Chances of Hands in Varying Suits')
    plt.xticks(index + bar_width,  ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    plt.legend()

    # plt.savefig('change_suits.pdf')
    plt.savefig('changes_suits.png')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()


