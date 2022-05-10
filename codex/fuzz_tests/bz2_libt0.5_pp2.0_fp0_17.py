import bz2
bz2.BZ2File(filepath)

# read the file into a list to eliminate trailing whitespace characters
with bz2.BZ2File(filepath) as f:
    data = f.readlines()

# replace sub-strings
data = [x.replace("\n", " ") for x in data]

# remove the trailing whitespace characters
data = [x.strip() for x in data]

# join the list into a string
data_string = ''.join(data)

# split the string into words
data_words = data_string.split()

# create a Counter object
from collections import Counter

# count the number of times each word occurs in the text and store the results in a dictionary called word_counts
word_counts = Counter(data_words)

# print the total number of words in the corpus
print(sum(word_counts.values()))

# print the number of unique words in the corpus
print(len(word_counts))

# print the 10 most frequently appearing words and their counts
print(word_counts.
