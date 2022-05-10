import bz2
bz2.BZ2File('./data/train.ft.txt.bz2').read()

#%%
import pandas as pd
import re

def text_to_df(text):
    pattern = re.compile(r'__label__(\d+)')
    labels = [pattern.findall(line) for line in text.split('\n')]
    return pd.DataFrame(labels, columns=['label'])

df = text_to_df(text)
df['label'].value_counts()

#%%
import spacy
nlp = spacy.load('en')

def text_to_tokens(text):
    return [token.text for token in nlp(text)]

df['tokens'] = df['text'].apply(text_to_tokens)
df.head()

#%%
from gensim.models import Word2Vec

sentences = df['tokens'].tolist()
model = Word2Vec(sentences, size=100, window=5
