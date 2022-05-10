import bz2
bz2_file = bz2.BZ2File('../data/wiki/en/wiki-en-full.txt.bz2')
data = bz2_file.read()
data = data.split('\n')
data = [line.split(' ') for line in data]

print data[:3]
 

# Save the text in a file, one article per line
# and use the pickle module to store the article lengths in a file.

# Use a list comprehension to select articles of at least 1000 tokens.

# Create a new list by stripping all tokens of their numbers and punctuation.

# Use a list comprehension to split each article into a list of words. 
# Note that the words should be lower case.

# Create a dictionary that maps each word to a list of articles in which it occurs,
# where the article is represented by its index in the data list

# Write a function that takes an index and a word and returns the number of times
# the word occurs in the article represented by the index. 
# (Hint: Use the dictionary to find all articles that contain the word
