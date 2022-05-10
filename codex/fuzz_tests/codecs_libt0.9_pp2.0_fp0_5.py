import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

df = pd.read_csv(os.path.join('../data/', 'train_2km_labeling.csv'), header=0, index_col=0, engine='python') #, encoding='utf-8'
print(df.head())
print(df.shape)

y = np.zeros((len(df), 3))
y[:, 0] = np.array(df['error'])
y[:, 1] = np.array(df['keep_1'])
y[:, 2] = np.array(df['keep_2'])

train_X, test_X, train_y, test_y = train_test_split(df, y, test_size=0.3, stratify=y)
print(train_X.shape, test_X.shape)
print(train_y[:10])


# Preprocess text
train_texts = list(train_X['text'])
test_texts =
