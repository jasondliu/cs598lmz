import codecs
codecs.open('svm', 'w', 'ascii')

df0 = pd.read_csv('train0.txt', sep=" ", header=None)
df1 = pd.read_csv('train1.txt', sep=" ", header=None)

for i in range(5256):
    X = df0.drop([784], axis=1).sample(n=500)
    Y = df1.drop([784], axis=1).sample(n=500)
    X['label'] = 0
    Y['label'] = 1
    X_Y = pd.concat([X, Y])

    X_train, X_test, y_train, y_test = \
        train_test_split(X_Y.drop('label', axis=1), X_Y['label'], test_size=0.20, random_state=42)

    scales = StandardScaler().fit(X_train)
    x_trains = scales.transform(X_train)
    x_tests = scales.transform(X_test)
    clf = svm
