import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%

def get_data(path):
    df = pd.read_csv(path, sep='\t', header=None)
    df.columns = ['ID', 'Text', 'Label']
    return df

#%%

def get_vocab(df):
    vocab = set()
    for i in range(len(df)):
        text = df.loc[i, 'Text']
        text = text.split()
        vocab.update(text)
    return vocab

#%%

def get_tokenizer(vocab, num_words):
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(vocab)
    return tokenizer

#%%

def get_sequences(tokenizer, df):
    sequences = tokenizer.texts_to_sequences(df['Text'])
    return sequences

#%%

def pad_
