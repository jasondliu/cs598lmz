from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#%%
# The compressed file is actually a tar file, so we'll need to decompress it and extract it.

from tarfile import open as taropen
tar = taropen(fileobj=BytesIO(data))
tar.extractall(path='data')

#%%
# Now, let's use the ``load_files`` function from scikit-learn to load the data.

from sklearn.datasets import load_files
reviews_train = load_files("data/aclImdb/train/")
text_train, y_train = reviews_train.data, reviews_train.target
print("type of text_train: {}".format(type(text_train)))
print("length of text_train: {}".format(len(text_train)))
print("text_train[6]:\n{}".format(text_train[6]))

#%%
# The data is stored as raw text (one string per file), and the target (the sentiment) is stored as a label (0 or 1). The target name gives the meaning of the labels
