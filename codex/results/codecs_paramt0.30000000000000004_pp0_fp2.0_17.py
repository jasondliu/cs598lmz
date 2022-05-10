import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load data
train_data = pd.read_csv('../data/train.csv', sep='\t', encoding='utf-8', quoting=csv.QUOTE_NONE, error_bad_lines=False)
test_data = pd.read_csv('../data/test.csv', sep='\t', encoding='utf-8', quoting=csv.QUOTE_NONE, error_bad_lines=False)

# Shuffle data
train_data = train_data.sample(frac=1).reset_index(drop=True)

# Split data into train and validation set
train_data, val_data = train_data[:int(len(train_data)*0.8)], train_data[int(len(train_data)*0.8):]

# Tokenize data
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(train_data['Phrase'].values)
train_sequences = tokenizer.texts
