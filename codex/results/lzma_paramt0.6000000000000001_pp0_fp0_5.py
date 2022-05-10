from lzma import LZMADecompressor
LZMADecompressor().decompress(pickle.load(open('data/train_image.pickle', 'rb')))

# write to file
# pickle.dump(train_image, open('data/train_image.pickle', 'wb'), protocol=4)

# read back pickled file
# train_image = pickle.load(open('data/train_image.pickle', 'rb'))
# train_image.shape

# pickle.dump(test_image, open('data/test_image.pickle', 'wb'), protocol=4)

# read back pickled file
# test_image = pickle.load(open('data/test_image.pickle', 'rb'))
# test_image.shape

# pickle.dump(train_label, open('data/train_label.pickle', 'wb'), protocol=4)

# read back pickled file
# train_label = pickle.load(open('data/train_label.pickle', 'rb'))
# train_label.shape

# pickle.dump(test_label, open
