import bz2
bz2.open

# Read in the raw data.
with bz2.open('train.ft.txt.bz2', 'rb') as f:
    data = [x.decode('utf-8') for x in f.readlines()]

# Split sentences into words, removing punctuation and, optionally,
# numbers.
def normalize_text(text):
    norm_text = text.lower()

    # Replace breaks with spaces
    norm_text = norm_text.replace('<br />', ' ')

    # Pad punctuation with spaces on both sides
    for char in ['.', '"', ',', '(', ')', '!', '?', ';', ':']:
        norm_text = norm_text.replace(char, ' ' + char + ' ')

    return norm_text

data = [normalize_text(text) for text in data]

# Build our dictionary and replace rare words with UNK token.
def build_dictionary(sentences, vocabulary_size):
    # Turn sentences (list of strings) into lists of words
    split_
