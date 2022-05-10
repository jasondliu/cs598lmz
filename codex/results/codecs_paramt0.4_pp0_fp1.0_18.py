import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# load the dataset
path = './data/'
files = ['yelp_academic_dataset_review.json']

df_list = []
for file in files:
    df_list.append(pd.read_json(path + file, lines=True, encoding='utf-8', errors='replace_with_space'))

df = pd.concat(df_list)

df.head()

# remove null values
df.dropna(inplace=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# remove non-english reviews
df = df[df['text'].apply(lambda x: is_english(x))]

# remove reviews with less than 20 characters
df = df[df['text'].apply(lambda x: len(x) >= 20)]

df.head()

# remove punctuation
df['text'] = df['text'].apply(lambda x: remove_punctuation(x))


