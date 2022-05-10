import bz2
bz2_file = bz2.BZ2File('../data/train.ft.txt.bz2')

# Read the file
raw_data = bz2_file.readlines()

# Convert it into a list
data = []
for line in raw_data:
    data.append(line.decode("utf-8"))

# Print first 5 observations
data[:5]

# Label first two observations as negative and next three observations as positive
labels = [0]*2 + [1]*3
labels

# Prepare the dataset
corpus = data
labels = np.array(labels)

# Split the dataset into training and validation datasets 
X_train, X_val, y_train, y_val = train_test_split(corpus, labels, test_size=0.2, random_state=42)

# Print the shape of training and validation datasets
print(X_train.shape, y_train.shape)
print(X_val.shape, y_val.shape)

# Import label encoder 
from
