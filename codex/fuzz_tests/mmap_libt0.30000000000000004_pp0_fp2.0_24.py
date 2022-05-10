import mmap
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -sys.maxsize - 1
    for row in range(len(arr) - 2):
        for col in range(len(arr[row]) - 2):
            top = sum(arr[row][col:col+3])
            mid = arr[row+1][col+1]
            bottom = sum(arr[row+2][col:col+3])
            hourglass = top + mid + bottom
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.
