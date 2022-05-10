import codecs
codecs.register_error(
    'replace_with_space',
    lambda e: (u' ', e.start + 1)
)

# Load the data
train_data = pd.read_csv('../input/train.tsv', sep='\t')
test_data = pd.read_csv('../input/test.tsv', sep='\t')

# Drop the columns we don't care about
train_data = train_data.drop(['price', 'train_id'], axis=1)
test_data = test_data.drop(['test_id'], axis=1)

# Make a list of all the columns that are strings
string_columns = []
for col in train_data.columns:
    if train_data[col].dtype == 'object':
        string_columns.append(col)

# Clean up the string columns
for col in string_columns:
    train_data[col] = train_data[col].str.strip().str.replace('\+', ' ').str.replace(r'[^\w\s]',
