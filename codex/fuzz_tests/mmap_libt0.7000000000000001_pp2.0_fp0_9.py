import mmap
import os
import sys
from collections import defaultdict as dd
import matplotlib.pyplot as plt
import pysam

# function for plotting bar graph of read lengths
def plot_read_lengths(read_lens):
    plt.bar(range(len(read_lens)), read_lens.values(), align='center')
    plt.xticks(range(len(read_lens)), read_lens.keys())
    plt.xlabel('Read Length')
    plt.ylabel('Number of Reads')
    plt.title('Read Lengths of R1 and R2')
    plt.tight_layout()
    plt.show()

# function for plotting bar graph of mapped and unmapped reads
def plot_mapped_read_lengths(mapped_read_lens):
    plt.bar(range(len(mapped_read_lens)), mapped_read_lens.values(), align='center')
    plt.xticks(range(len(mapped_read_lens)), mapped_read_lens
