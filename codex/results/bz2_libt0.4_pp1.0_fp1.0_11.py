import bz2
bz2.BZ2File('../data/train.ft.txt.bz2')

# read the data, this might take a while
with bz2.BZ2File('../data/train.ft.txt.bz2') as f:
    data_raw = f.readlines()

# data_raw is a list, with each element a review in string
# check the total number of reviews
print(len(data_raw))

# check the first review
print(data_raw[0])

# check the last review
print(data_raw[len(data_raw)-1])

# check the type of the first review
type(data_raw[0])

# convert the string to lower case
data_raw = [x.lower() for x in data_raw]

# check the first review again
print(data_raw[0])

# split each review into a list of words
data_raw = [x.split() for x in data_raw]

# check the first review again
print(data_raw[0])

# check the type of
