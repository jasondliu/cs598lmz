import mmap
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    bribe = 0
    for i in range(n):
        if q[i] - i > 3:
            return "Too chaotic"
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe += 1
    return bribe

