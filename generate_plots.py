"""
Chad Bloxham. CS 260P Project 2.
May 24, 2019.

This function creates a log-log plot of the average waste versus size of item list for
each algorithm. Text files were created in generate_data.py.
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_plots(n_file, waste_file):
    n = np.loadtxt(n_file, delimiter=' ')
    waste = np.loadtxt(waste_file, delimiter=' ')
    # convert list sizes and avg waste to log base 2 values
    logn = np.log2(n)
    log_waste = np.log2(waste)
    # plot labels and colors
    labels = ['Next Fit', 'First Fit', 'Best Fit', 'FF Decr', 'BF Decr']
    colors = ['b', 'r', 'y', 'm', 'g']

    for i in range(len(waste)):
        # plot waste for this algorithm
        plt.plot(logn, log_waste[i], '.', color=colors[i])
        # calculate linear regression slope
        lin_fit = np.polyfit(logn, log_waste[i], 1)
        slope = ', m = ' + str(lin_fit[0])[0:6]
        # convert linear regression into function
        lin_fit_fn = np.poly1d(lin_fit)
        # plot function
        plt.plot(logn, lin_fit_fn(logn), '--', color=colors[i], label=labels[i]+slope)
    # formatting
    plt.title('Waste of Bin Packing Algorithms')
    plt.xlabel('logN (base 2)')
    plt.ylabel('logW (base 2)')
    plt.legend(title='Algorithms', loc='upper left')
    plt.show()
