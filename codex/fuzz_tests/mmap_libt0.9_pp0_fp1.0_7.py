import mmap
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) < 2:
        return 0
    pos = 0
    count = 0
    while pos < len(c)-1:
        if pos <= len(c) - 3 :
            if c[pos + 2] == 0:
                pos += 2
                count += 1
            else:
                pos += 1
                count += 1
        else:
            pos += 1
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
