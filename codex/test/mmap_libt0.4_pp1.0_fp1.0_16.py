import mmap
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] != i+1:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            swaps += 1
        else:
            i += 1
    return swaps

