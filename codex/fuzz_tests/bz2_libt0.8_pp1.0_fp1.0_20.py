import bz2
bz2.encoders.encode_bytearray

# Data Set
data = ' '.join(brown.words()[:5000])

labels = list(set(data))  # set of unique chars
labels.sort()

labels_map = {l: i for i, l in enumerate(labels)}  # map each unique char to a number
text_map = [labels_map[c] for c in data]  # map each char in data to numbers

# Create train and test data
slice_len = 3

X = np.zeros((len(data), slice_len, len(labels)), dtype=np.bool)
y = np.zeros((len(data), len(labels)), dtype=np.bool)
for i in range(len(data) - slice_len):
    X[i, :, :][list(map(lambda s: labels_map[s], data[i:i+slice_len]))] = 1
    y[i, :][labels_map[data[i+slice_len]]] =
