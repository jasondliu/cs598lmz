import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Load the dictionary
with open(sys.argv[1], 'r') as f:
    dictionary = json.load(f)

# Load the corpus
with codecs.open(sys.argv[2], 'r', 'utf-8', 'strict') as f:
    corpus = f.read()

# Split the corpus into sentences
sentences = corpus.split('\n')

# Split the sentences into words
words = [sentence.split(' ') for sentence in sentences]

# Remove empty sentences
words = [sentence for sentence in words if sentence != ['']]

# Remove empty words
words = [[word for word in sentence if word != ''] for sentence in words]

# Remove words not in the dictionary
words = [[word for word in sentence if word in dictionary] for sentence in words]

# Remove empty sentences
words = [sentence for sentence in words if sentence != []]

# Remove duplicates
words = [list(set(sentence)) for sentence in words]

# Output the result
with
