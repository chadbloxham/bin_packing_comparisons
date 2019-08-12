"""
Chad Bloxham. CS 260P Project 2.
May 24, 2019.

Main file for a set of programs which compare the performance of different bin
packing algorithms: Next Fit, First Fit, Best Fit, First Fit Decreasing, and Best
Fit Decreasing. See bin_packing.py for a description of each algorithm.

The performance of an algorithm is defined as how little waste it produces:

                        waste = num_bins - sum(item_sizes)

i.e. number of bins (capacity 1) needed to pack a list of items minus the sum
of the sizes of those items (each item has a size between 0.0 and 0.8)

The waste is calculated using various item list sizes for each algorithm.

This file generates the data text files if they do not already exist and creates
the waste plot.
"""

# import needed functions and modules
from generate_plots import *
from generate_data import *
import os.path


def main():
    # generate the waste data only if it has not been already generated
    if not (os.path.exists('n.txt') and os.path.exists('avg_waste.txt')):
        generate_data()
    # plot data
    generate_plots('n.txt', 'avg_waste.txt')


if __name__ == "__main__":
    main()
