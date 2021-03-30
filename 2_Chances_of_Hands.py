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
2. Chances of Hands
'''


'''
2.1 Test Pair Rate
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

def pair_test():
    '''
    Draw a hand from a draw shuffled deck, and test whether there is a pair
    :return: if there is a pair, return 1, otherwise return 0.
    '''
    my_deck = Deck(1, 13, 4)
    my_deck.shuffle()
    hand_list = []
    for i in range(5):
        hand_list.append(my_deck[i])
    if is_pair(hand_list) == True:
        return 1
    else:
        return 0

def get_pair_rate(pairTest_size = 1000):
    '''
    draw a hand from a random shuffled deck n times,
    return the approximated probability of getting a pair
    :param pairTest_size: times of random draw
    :return: the approximated probability of getting a pair
    '''
    pairTest_result = []
    for i in range(pairTest_size):
        newValue = pair_test()
        pairTest_result.append(newValue)
    pair_rate = sum(pairTest_result) / pairTest_size
    # uncomment to print data
    # transposedMatrix = np.transpose(pairTest_result)
    # print (transposedMatrix)
    return pair_rate



'''
2.2 Test Flush Rate
'''

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

def flush_test():
    '''
     Draw a hand from a draw shuffled deck,
     and test whether there is a flush
     :return: if there is a flush, return 1, otherwise return 0.
     '''
    my_deck = Deck(1, 13, 4)
    my_deck.shuffle()
    hand_list = []
    for i in range(5):
        hand_list.append(my_deck[i])
    if is_flush(hand_list) == True:
        return 1
    else:
        return 0

def get_flush_rate(flushTest_size = 1000):
    '''
     draw a hand from a random shuffled deck n times,
     return the approximated probability of getting a pair
     :param pairTest_size: times of random draw
     :return: the approximated probability of getting a pair
     '''
    flushTest_result = []
    for i in range(flushTest_size):
        newValue = flush_test()
        flushTest_result.append(newValue)
    flush_rate = sum(flushTest_result) / flushTest_size
    # uncomment to print data
    # transposedMatrix = np.transpose(flushTest_result)
    # print (transposedMatrix)
    return flush_rate



def main():
    print(get_pair_rate())
    print(get_flush_rate())

    ###############
    # Plot the Data
    ###############

    # data to plot
    n_groups = 2
    success = (get_pair_rate(), get_flush_rate())
    failure = (1 - get_pair_rate(), 1-get_flush_rate())

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    success_bar = plt.bar(index, success, bar_width,
                          alpha=opacity, color='b', label='Success')

    failure_bar = plt.bar(index + bar_width, failure, bar_width,
                          alpha=opacity, color='g', label='Failure')

    plt.xlabel('Results')
    plt.ylabel('Number of Trails')
    plt.title('Chances of Hands')
    plt.xticks(index + bar_width,  ('Pair', 'Flush'))
    plt.legend()

    # plt.savefig('pair_flush.pdf')
    plt.savefig('pair_flush.png')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()