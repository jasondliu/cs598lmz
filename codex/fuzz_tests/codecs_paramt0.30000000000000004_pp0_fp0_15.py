import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# load the data
train_data = pd.read_csv('../data/train.csv', encoding='utf-8', sep=',', error_bad_lines=False)
test_data = pd.read_csv('../data/test.csv', encoding='utf-8', sep=',', error_bad_lines=False)

# drop the columns that are not useful
train_data.drop(['id', 'qid1', 'qid2', 'is_duplicate'], axis=1, inplace=True)
test_data.drop(['test_id'], axis=1, inplace=True)

# concatenate the data
data = pd.concat([train_data, test_data], axis=0)

# replace the missing values with empty string
data.fillna('', inplace=True)

# create a new column that contains the length of question1
data['q1_len'] = data['question1'].apply(lambda x: len(x))


