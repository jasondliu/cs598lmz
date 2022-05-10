import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load the data
train_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t', error_bad_lines=False, warn_bad_lines=False)
test_data = pd.read_csv('test.csv', encoding='utf-8', sep='\t', error_bad_lines=False, warn_bad_lines=False)

# Remove the missing data
train_data = train_data.dropna()
test_data = test_data.dropna()

# Remove the duplicates
train_data.drop_duplicates(subset='text', inplace=True)
test_data.drop_duplicates(subset='text', inplace=True)

# Remove the extra spaces
train_data['text'] = train_data['text'].apply(lambda x: x.strip())
test_data['text'] = test_data['text'].apply(lambda x: x.strip())

# Remove the special characters
train_data['text
