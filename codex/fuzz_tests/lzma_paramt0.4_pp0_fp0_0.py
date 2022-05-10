from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress data
decompressed_data = lzma.decompress(data)
# convert from bytes to string
text = decompressed_data.decode('utf-8')
# split string into a list of lines
lines = text.splitlines()
# display the first 5 lines
lines[:5]

# display the last 5 lines
lines[-5:]

# join the lines back into one string
big_string = ' '.join(lines)
# display the first 1000 characters
big_string[:1000]

# split the string into individual words
words = big_string.split()
# display the first 10 words
words[:10]

# create a Counter to store the words and count of each word
word_counts = Counter(words)
# display the 10 most common words and their counts
word_counts.most_common(10)

# find the total number of words
total_num_words = len(words)
# calculate the frequency of each word
word_freqs = {word: count/total_num_words for
