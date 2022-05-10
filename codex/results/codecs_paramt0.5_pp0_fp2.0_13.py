import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# Read the data
df = pd.read_csv('../data/raw/train.csv')

# Get rid of the id column
df.drop('id', axis=1, inplace=True)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df['comment_text'], df['toxic'], test_size=0.33, random_state=42)

# Create the tokenizer
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(X_train)

# Convert text to sequences
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

# Pad the sequences
X_train = pad_sequences(X_train, maxlen=MAX_SEQUENCE_LENGTH)
X_test = pad_sequences(X_test, maxlen=
