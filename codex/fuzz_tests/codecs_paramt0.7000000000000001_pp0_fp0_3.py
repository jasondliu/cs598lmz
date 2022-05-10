import codecs
codecs.register_error("pass-through", lambda e: (u"\ufffd", e.start + 1))

logging.basicConfig(level=logging.INFO)

logging.info("Loading data...")

# Load data from the IMDB dataset
train_texts, train_labels, test_texts, test_labels = load_imdb_sentiment_analysis_dataset()

# Create Tokenizer object
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(train_texts)

# Pad sequences
train_tokens = tokenizer.texts_to_sequences(train_texts)
test_tokens = tokenizer.texts_to_sequences(test_texts)

train_data = pad_sequences(train_tokens, maxlen=MAX_SEQUENCE_LENGTH, padding='pre', truncating='pre')
test_data = pad_sequences(test_tokens, maxlen=MAX_SEQUENCE_LENGTH, padding='pre', truncating
