import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

# Load the data
data = np.load('../../data/data_with_features.npz')
X = data['X']
Y = data['Y']

# Preprocess the data
X, Y = shuffle(X, Y)
Y = Y[:, np.newaxis]
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.8)
X_train, Y_train = X[:offset], Y[:offset]
X_test, Y_test = X[offset:], Y[offset:]

# Initialize the model
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

