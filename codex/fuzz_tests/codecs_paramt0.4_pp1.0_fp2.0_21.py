import codecs
codecs.register_error('unexpected', codecs.lookup_error('ignore'))

# read in the file
with codecs.open(file, 'r', 'utf-8', 'unexpected') as f:
    text = f.read()

# split the file into lines
lines = text.split('\n')

# create a list of the words in the file
words = []
for line in lines:
    words += line.split(' ')

# clean up the words
# remove empty strings
words = [word for word in words if word != '']
# remove punctuation
words = [word.strip(string.punctuation) for word in words]
# remove digits
words = [word for word in words if not word.isdigit()]
# make all words lowercase
words = [word.lower() for word in words]

# create a list of the unique words in the file
unique_words = list(set(words))

# create a dictionary of the words and their frequencies
word_freq = {}
for word in words:
    if word in word_freq:

