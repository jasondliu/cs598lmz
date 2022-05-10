import mmap
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    for i in range(len(queries)):
        result.append(strings.count(queries[i]))
    return result

