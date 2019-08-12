# bin_packing_comparisons
Chad Bloxham

May 2019

## Purpose
Python program which computes and displays the performance of various bin-packing algorithms. See bin_packing.py for information regarding the particular algorithms. The performance of a bin-packing algorithm is how little waste it produces. For an input list of item sizes (ranging from 0.0 to 0.8), the waste of an algorithm is the number of bins (with capacity 1.0) it uses to pack all items minus the sum of item sizes i.e. waste = num_bins - sum(item_sizes).

## Run Instructions
Requires the Numpy library, Matplotlib library, os library, and any version of Python which supports them. Run Main.py.

## Main.py output
![waste plot](https://github.com/chadbloxham/bin_packing_comparisons/blob/master/waste_plot.png)
