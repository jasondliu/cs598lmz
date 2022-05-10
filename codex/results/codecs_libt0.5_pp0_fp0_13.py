import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Load data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Create target variable
train["is_duplicate"] = train["is_duplicate"].apply(lambda x: 1 if x == 1 else 0)

# Load the training dataset
train_qs = pd.Series(train['question1'].tolist() + train['question2'].tolist()).astype(str)

# Load the test dataset
test_qs = pd.Series(test['question1'].tolist() + test['question2'].tolist()).astype(str)

# Calculate the distribution of words in the training dataset
dist_train = train_qs.apply(lambda x: len(x.split(' ')))
plt.figure(figsize=(15, 10))
plt.hist(dist_train, bins=50, range=[0, 50], color=
