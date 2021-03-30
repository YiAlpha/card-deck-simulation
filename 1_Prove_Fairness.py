###################################
# Assignment 3
###################################

from deck import Deck
import pylab
import random
import numpy as np
import matplotlib.pyplot as plt

# set seed to reproduce the random draw result
random.seed(1005)


'''
1.Proving Fairness
'''

'''
1.1. Random Draw 1000 times
'''
def mean_value(size = 1000):
    my_deck = Deck(1, 13, 4)
    my_deck.shuffle()

    # get face index for each card
    face_list=[]
    for i in range(52):
        face_list.append(my_deck.draw_card().get_face_index())

    # Random draw from a deck of cards 1000 times
    sample_result =  random.choices(face_list, k=1000)
    mean_result = np.mean(sample_result)

    return mean_result, sample_result



'''
1.2. Repeat experiment to show sampling distribution of sample mean
'''
# Write a function to repeat 1000 draws
# Set default to test 10-time repeat
def mean_test(meanTest_size = 10):
    meanTest_result = []
    for m in range(meanTest_size):
        test_deck = Deck(1, 13, 4)
        test_deck.shuffle()
        face_list = []
        for i in range(52):
            face_list.append(test_deck.draw_card().get_face_index())
        sample_result = random.choices(face_list, k=1000)

        newValue =  np.mean(sample_result)
        meanTest_result.append(newValue)
    return meanTest_result



def main():
    # Mean face value of 1000 draw
    mean_result, sample_result = mean_value()
    print(mean_result)

    # Uncomment to print the data
    # transposedMatrix = np.transpose(sample_result)
    # print(transposedMatrix)


    ################
    # Plot histogram
    ################
    pylab.hist(sample_result, 100)
    pylab.xlabel('Face Value')
    pylab.ylabel('Count of Success')
    plt.xticks(np.arange(min(sample_result), max(sample_result) + 1, 1.0))
    # pylab.savefig('single_1.pdf')
    pylab.savefig('figure_1.png')
    pylab.show()

    # repeat the experiment above 100000 times, save every mean to the list
    run_result = mean_test(100000)

    # Plot the mean test results
    t = np.arange(1, 100001, 1)
    plt.plot(t, run_result, 'g.', markersize=0.7)
    # pylab.savefig('multiple_ori.pdf')
    pylab.savefig("figure_2.png')
    plt.show()

if __name__ == '__main__':
    main()
