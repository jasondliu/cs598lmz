import codecs
codecs.getreader("utf-8")(sys.stdin).readline()
import numpy as np

# This code assumes the data is stored as a numpy array with shape (n, 20)
# n is the length of the input; 20 is the length of the smallest allowed
# semantic prototypes
#

inputs = data[:,:-1]
output_labels = data[:,-1]

# 1. A Dictionary of Lists
# 2. Each element of the dictionary is a list
# 3. Each element of these lists must be a tuple, with first element the number
#    of the group the data point belongs to
# 4. The second element of the tuple is the data point

# Preprocess data according to the assumptions
groups = []
for i in range(inputs.shape[0]):
    if i == 0:
        groups.append([])
        groups[0].append(i)
    if i > 0:
        isInGroup = 0
        for j in range(len(groups)):
            for k in range(len(groups[j])):
                if all(abs
