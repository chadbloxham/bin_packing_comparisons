"""
Chad Bloxham. CS 260P Project 2.
May 24, 2019.

This function calculates the average waste (five runs) produced by each bin-packing
algorithm for each item list size.
"""

from bin_packing import *
import numpy as np


def generate_data():
    # list sizes will be factors of 2 ranging from 2^4 to 2^14
    min_exp = 4
    max_exp = 14
    n = [2**i for i in range(min_exp, max_exp+1)]
    n = np.array(n, dtype=np.int)
    num_algs = 5
    # (next_fit, first_fit, best_fit, ff_decr, bf_decr)
    avg_waste = np.empty((num_algs, len(n)), dtype=np.float)
    # calculate waste averages for each algorithm
    for i in range(len(n)):
        waste_sum = np.float(0.0)
        for j in range(5):
            items = generate_items(n[i])
            waste = next_fit(items)[0]
            waste_sum += waste
        avg_waste[0, i] = waste_sum / 5.0
        waste_sum = np.float(0.0)
        for j in range(5):
            items = generate_items(n[i])
            waste = first_fit(items)[0]
            waste_sum += waste
        avg_waste[1, i] = waste_sum / 5.0
        waste_sum = np.float(0.0)
        for j in range(5):
            items = generate_items(n[i])
            waste = best_fit(items)[0]
            waste_sum += waste
        avg_waste[2, i] = waste_sum / 5.0
        waste_sum = np.float(0.0)
        for j in range(5):
            items = generate_items(n[i])
            waste = first_fit(items, decr=True)[0]
            waste_sum += waste
        avg_waste[3, i] = waste_sum / 5.0
        waste_sum = np.float(0.0)
        for j in range(5):
            items = generate_items(n[i])
            waste = best_fit(items, decr=True)[0]
            waste_sum += waste
        avg_waste[4, i] = waste_sum / 5.0

    # save data to text files
    np.savetxt('n.txt', n)
    np.savetxt('avg_waste.txt', avg_waste)
