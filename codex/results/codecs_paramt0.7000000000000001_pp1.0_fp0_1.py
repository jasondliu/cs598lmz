import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)
# sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='surrogate_escape')
# sys.stdout = codecs.getwriter('utf8')(sys.stdout.detach(), errors='surrogate_escape')

import os
import pandas as pd

# df = pd.read_csv('../../data/train.csv')
df = pd.read_csv('../../data/train.csv', encoding='utf-8')
counts = df['author'].value_counts()
authors = counts.index

# with open('../../data/train/authors.txt', 'w') as f:
#     for author in authors:
#         f.write(author.replace(' ', '_') + '\n')

# for author in authors:
#     os.mkdir('../../data/train/' + author.replace(' ', '_'))

# for index, row in df.iterrows():
#
