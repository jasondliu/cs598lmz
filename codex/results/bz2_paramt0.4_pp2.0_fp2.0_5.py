from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# %%
# The data is a string of bytes.  We can convert it to a string of characters
# by decoding it.

text = data.decode('utf-8')

# %%
# Now we can print the first 300 characters of the text.

print(text[:300])

# %%
# We can also split the text into a list of words.

words = text.split()

# %%
# And count the number of words.

len(words)

# %%
# We can use the Counter class from the collections module to count the words.

from collections import Counter

counter = Counter(words)

# %%
# Here are the top 10 most common words.

counter.most_common(10)

# %%
# We can use a dictionary comprehension to create a dictionary that maps from each word to the number of times it appears in the text.

hist = {word: count for word, count in counter.most_common()}

# %%
# Here are the first 10 words and their frequencies.

{k: hist
