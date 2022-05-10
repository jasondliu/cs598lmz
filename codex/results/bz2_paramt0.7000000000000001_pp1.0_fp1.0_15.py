from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../../data/train.csv.bz2').read())

pd.read_csv('../../data/train.csv')

import bz2
with bz2.BZ2File('../../data/train.csv.bz2') as f:
    for line in f:
        print(line)
        break

# let's get the first line from the file
filename = '../../data/train.csv.bz2'
pd.read_csv(filename, nrows=1)

# what if we want to read a small percentage of the file?

# we can use chunksize to specify how many lines to read in at a time
pd.read_csv(filename, nrows=5, chunksize=3)

# let's iterate through the file
# we'll set up a counter and a list to store information
n = 5000000
skip = sorted(random.sample(range(1, 8925083), 8925083 - n))

# now let's use the skip parameter in read_csv
# we'll specify that we
