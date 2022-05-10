from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(c)

# pickled train data
s = pickle.load(open('train.pickle', 'rb'))
X_train = s['X_train']
y_train = s['y_train']
del s
pickle.dump(X_train, open('X_train.pickle', 'wb'))
del X_train
pickle.dump(y_train, open('y_train.pickle', 'wb'))
del y_train

# pickled test data
s = pickle.load(open('test.pickle', 'rb'))
X_test = s['X_test']
y_test = s['y_test']
del s
pickle.dump(X_test, open('X_test.pickle', 'wb'))
del X_test
pickle.dump(y_test, open('y_test.pickle', 'wb'))
del y_test

# train_modified.csv
c = bz2.BZ2File('../input/train_modified.csv.bz2', 'rb
