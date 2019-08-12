"""
Chad Bloxham. CS 260P Project 2.
May 24, 2019.

This file implements each bin packing algorithm as a function which takes
a list of items as input.
"""

import numpy as np


# input for each algorithm - each item has size between 0.0 and 0.8
def generate_items(n):
    items = np.random.uniform(0.0, 0.8, n)
    return items


# Next Fit Algorithm. Only one bin available at a time. If the next item
# does not fit in this bin, open a new bin to place the item.
def next_fit(input_items):
    items = np.array(input_items, dtype=np.float)
    item_sum = np.sum(items)
    num_bins = 1
    current_bin = 0
    for item in items:
        # place item in bin if it fits
        if item + current_bin <= 1:
            current_bin += item
        # if not, open new bin and place item
        else:
            num_bins += 1
            current_bin = item
    waste = num_bins - item_sum
    return waste, num_bins


# First Fit Algorithm: multiple bins available for placement. Place next item in the first bin
# which can hold it. Decreasing version: sort item sizes in desceding order before packing starts.
def first_fit(input_items, decr=False):
    items = np.array(input_items, dtype=np.float)
    item_sum = np.sum(items)
    # sort in descending order if specified
    if decr:
        items = np.sort(items)[::-1]
    bins = [0]  # only one empty bin initially
    for item in items:
        bin_found = False
        i = 0
        # test if item fits in this bin
        while not bin_found and i < len(bins):
            if item + bins[i] <= 1:
                bins[i] += item
                bin_found = True
            else:
                i += 1
        # if item fit in none, open new bin
        if i == len(bins):
            bins.append(item)
    waste = len(bins) - item_sum
    return waste, len(bins)


# Best Fit: multiple bins open for placement. Place next item in the bin in which it fits best
# i.e. leaves the least amount of remaining room. Decreasing version same as above.
def best_fit(input_items, decr=False):
    items = np.array(input_items, dtype=np.float)
    item_sum = np.sum(items)
    # sort in descending order if specified
    if decr:
        items = np.sort(items)[::-1]
    bins = [0]  # only one empty bin initially
    for item in items:
        # find remaining space in each bin if item were placed
        diffs = []
        for bin_val in bins:
            diffs.append(1 - (bin_val + item))
        diffs = np.array(diffs)
        # isolate bins which have remaining space (positive difference)
        mask = diffs >= 0
        pos_diffs = diffs[mask]
        if len(pos_diffs) == 0:
            bins.append(item)
        else:
            # find bin with least amount of space remaining
            min_pos = np.min(pos_diffs)
            bin_num = np.argwhere(diffs == min_pos)[0][0]
            bins[bin_num] += item
    waste = len(bins) - item_sum
    return waste, len(bins)
