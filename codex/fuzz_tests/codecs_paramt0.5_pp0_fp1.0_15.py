import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Create the dictionary
vocab_dict = {}
# Create a generator for the file
# Note that you can't re-read the file generatively with this method
f = open('vocab.txt')
for line in f:
    (key, val) = line.split()
    vocab_dict[key] = int(val)
f.close()

# Read the test data
test_data = []
test_labels = []
f = codecs.open('testdata.txt', encoding='utf-8', errors='replace_with_space')
for line in f:
    line = line.strip()
    if not line:
        continue
    label, text = line.split('\t', 1)
    words = text.split()
    # Convert to lowercase
    words = [word.lower() for word in words]
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    # Stem words
    words = [stemmer.stem(word)
