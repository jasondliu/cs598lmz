import lzma
# Test LZMADecompressor
with lzma.open('TrainingDataset/X_train.txt.xz') as f:
    file_content = f.read()

 
# Load data 
X_train = np.loadtxt('TrainingDataset/X_train.txt')
y_train = np.loadtxt('TrainingDataset/y_train.txt')

X_test = np.loadtxt('TestDataset/X_test.txt')
y_test = np.loadtxt('TestDataset/y_test.txt')
start_time = time.time()
# you can use any other residual network.
model = ResNet50(weights='imagenet', classes=len(label_class.keys()))

# loading the dataset and making the classification.
model.fit(X_train, y_train,
          epochs=10, verbose=1,
          validation_data=(X_test, y_test))

# evaluating the performance.
score = model.evaluate(X_test, y_test, verbose=0)

model.summary()
print('
