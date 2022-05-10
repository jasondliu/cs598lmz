import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load data
train_data = pd.read_csv('data/train.csv', sep=',', encoding='utf-8', error_bad_lines=False)
test_data = pd.read_csv('data/test.csv', sep=',', encoding='utf-8', error_bad_lines=False)

# Remove non-alphabetic characters
train_data['text'] = train_data['text'].str.replace('[^a-zA-Z]', ' ')
test_data['text'] = test_data['text'].str.replace('[^a-zA-Z]', ' ')

# Convert all characters to lowercase
train_data['text'] = train_data['text'].str.lower()
test_data['text'] = test_data['text'].str.lower()

# Remove stopwords
stop_words = set(stopwords.words('english'))
train_data['text'] = train_data['text'].apply(lambda x: ' '.
