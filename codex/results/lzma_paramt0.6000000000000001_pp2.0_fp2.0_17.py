from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# return a list of all of the words in the data, converted to lower case and
# with the punctuation removed
def get_words(data):
    return re.findall(r'\w+', data.lower())

# return a list of all of the words in the data, converted to lower case and
# with the punctuation removed
def get_words(data):
    return re.findall(r'\w+', data.lower())

# return a dictionary with the words of the data as the keys and their number of
# occurrences as the values
def get_word_counts(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

# return a list of the top n most common words in the data
def get_top_n_words(counts, n):
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]

# returns the list of words, count dictionary, and top n words in
