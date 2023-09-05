""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Huimin Liu  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: hliu749 		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903850497 		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "hliu749"  # replace tb34 with your Georgia Tech username.
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 903850497  # replace with your GT ID number
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 18/38  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		  		 		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  		 		  		  		    	 		 		   		 		  
    # add your code here to implement the experiments  	#

    bank_roll = 256

    exp1_figure1(win_prob)
    exp1_figure2_and_figure3(win_prob)
    exp2_figure4_and_figure5(win_prob, bank_roll)


def simulator(win_prob, has_bankroll, bankroll):
    # init the array with 80 so that after we win early, we don't need to populate the rest
    result_array = np.full((1001), 80)
    episode_winnings = 0

    count = 0
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            if count >= 1001:
                return result_array
            result_array[count] = episode_winnings
            count += 1
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2

                if has_bankroll:

                    # if last round went all in
                    if episode_winnings == -bankroll:
                        # populate the rest of array
                        result_array[count:] = episode_winnings
                        return result_array

                    if episode_winnings - bet_amount < -bankroll:
                        # all in the left
                        bet_amount = bankroll + episode_winnings

    return result_array


def exp1_figure1(win_prob):
    # run simulator 10x and plot winnings
    # starting from 0
    # 10 arrays needed for graph
    # plot all 10 runs on one chart using matplotlib functions
    # horizontal axis should range from 0 to 300, vertical axis from -256 to +100
    # 10 lines in total

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 1 - 10 trials w/ infinite bankroll")
    plt.xlabel("Number of Trials")
    plt.ylabel("Total Winnings")

    for index in range(10):
        curr_episode = simulator(win_prob, False, None)
        plt.plot(curr_episode)
    # result_array[index] = curr_episode

    plt.savefig("figure1.png")
    plt.clf()


# return result_array

def exp1_figure2_and_figure3(win_prob):
    # run simulator 1000x and plot the mean value of winnings
    # starting from 0
    # 3 arrays (mean, mean +sd, mean -sd) needed for graph
    # plot all 1000 runs and +- sd on one chart using matplotlib functions
    # horizontal axis should range from 0 to 300, vertical axis from -256 to +100
    # three lines in total

    result_array = np.zeros((1000, 1001))
    for index in range(1000):
        curr_episode = simulator(win_prob, False, None)
        result_array[index] = curr_episode

    """
    # print the last element of every episode
    # print(result_array[:, -1])
    """

    ### plot figure 2

    # 1. calculations
    mean_array = np.mean(result_array, axis=0)
    std = np.std(result_array, axis=0)
    mean_plus_array = mean_array + std
    mean_minus_array = mean_array - std

    # 2. plot setup
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 2 - means of 1000 trials w/ infinite bankroll")
    plt.xlabel("Number of Trials")
    plt.ylabel("Total Winnings")

    # 3. plotting!
    plt.plot(mean_array, label="mean")
    plt.plot(mean_plus_array, label="mean+std")
    plt.plot(mean_minus_array, label="mean-std")

    # 4. saving and clearing
    plt.legend()
    plt.savefig("figure2.png")
    plt.clf()

    ### plot figure 3

    median_array = np.median(result_array, axis=0)
    std = np.std(result_array, axis=0)
    median_plus_array = median_array + std
    median_minus_array = median_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 3 - medians of 1000 trials w/ infinite bankroll")
    plt.xlabel("Number of Trials")
    plt.ylabel("Total Winnings")

    plt.plot(median_array, label="median")
    plt.plot(median_plus_array, label="median+std")
    plt.plot(median_minus_array, label="median-std")
    plt.legend()
    plt.savefig("figure3.png")
    plt.clf()


def exp2_figure4_and_figure5(win_prob, bank_roll):
    result_array = np.zeros((1000, 1001))
    for index in range(1000):
        curr_episode = simulator(win_prob, True, bank_roll)
        result_array[index] = curr_episode

    """
    end_array = result_array[:, -1]
    print(end_array)
    print(list(end_array).count(80))
    print(list(end_array).count(-256))
    """

    ### plot figure 4
    mean_array = np.mean(result_array, axis=0)
    std = np.std(result_array, axis=0)
    mean_plus_array = mean_array + std
    mean_minus_array = mean_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 4 - means of 1000 trials w/ $" + str(bank_roll) + " bankroll")
    plt.xlabel("Number of Trials")
    plt.ylabel("Total Winnings")

    plt.plot(mean_array, label="mean")
    plt.plot(mean_plus_array, label="mean+std")
    plt.plot(mean_minus_array, label="mean-std")

    plt.legend()
    plt.savefig("figure4.png")
    plt.clf()

    ### plot figure 5
    median_array = np.median(result_array, axis=0)
    std = np.std(result_array, axis=0)
    median_plus_array = median_array + std
    median_minus_array = median_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 5 - medians of 1000 trials w/ $" + str(bank_roll) + " bankroll")
    plt.xlabel("Number of Trials")
    plt.ylabel("Total Winnings")

    plt.plot(median_array, label="median")
    plt.plot(median_plus_array, label="median+std")
    plt.plot(median_minus_array, label="median-std")
    plt.legend()
    plt.savefig("figure5.png")
    plt.clf()



if __name__ == "__main__":
    # print the whole matrix without scientific formatting
    np.set_printoptions(threshold=10000000000000, suppress=True)

    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
