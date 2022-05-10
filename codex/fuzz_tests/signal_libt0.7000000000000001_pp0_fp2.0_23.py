import signal
signal.alarm(5)

import numpy as np
import time

# read input
line1 = input()
line2 = input()

# parse input
N = int(line1.split()[0])
# data = list(map(int, line2.split()))
data = np.array(list(map(int, line2.split())))

# initialize
max_sum = data[0]
max_sum_begin = 0
max_sum_end = 0
current_sum = data[0]
current_sum_begin = 0
for i in range(1, N):
    # update current_sum
    current_sum += data[i]

    # update max_sum
    if current_sum > max_sum:
        max_sum = current_sum
        max_sum_begin = current_sum_begin
        max_sum_end = i

    # if current_sum < 0 then reset
    if current_sum < 0:
        current_sum = 0
        current_sum_begin = i+1

# print output
print(max
