import bz2
bz2_file = bz2.BZ2File('../data/train.ft.txt.bz2')
train_file = bz2_file.readlines()

# Read test file
bz2_file = bz2.BZ2File('../data/test.ft.txt.bz2')
test_file = bz2_file.readlines()

# Create a list of labels
labels = []
for line in train_file:
    label = line.split(' ')[0]
    if label == '__label__1':
        labels.append(1)
    else:
        labels.append(0)

# Create a list of sentences
sentences = []
for line in train_file:
    sentence = line.split(' ', 1)[1][:-1].lower()
    sentences.append(sentence)

for line in test_file:
    sentence = line.split(' ', 1)[1][:-1].lower()
    sentences.append(sentence)

# Create a list of words
words = " ".join(sentences).split
