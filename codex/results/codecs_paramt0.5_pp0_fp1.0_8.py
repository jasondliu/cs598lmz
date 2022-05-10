import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load the data
print("Loading data...")

# The training data.
train_data = list(codecs.open(train_data_file, 'r', 'utf-8', 'replace_with_space').readlines())
train_data = [s.strip() for s in train_data]

# The test data.
test_data = list(codecs.open(test_data_file, 'r', 'utf-8', 'replace_with_space').readlines())
test_data = [s.strip() for s in test_data]

# The training labels.
train_labels = list(codecs.open(train_label_file, 'r', 'utf-8', 'replace_with_space').readlines())
train_labels = [s.strip() for s in train_labels]

# The test labels.
test_labels = list(codecs.open(test_label_file, 'r', 'utf-8', 'replace_with_space
