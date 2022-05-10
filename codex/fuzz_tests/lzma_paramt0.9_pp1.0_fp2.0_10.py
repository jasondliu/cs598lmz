from lzma import LZMADecompressor
LZMADecompressor.format = None

import os
import pandas as pd

df = pd.read_table("SQuAD-v1.1-train.txt.question", delimiter='\n', names=["question"])
df.head()

sent_detector = nltk.data.load('tokenizers/punkt/portuguese.pickle')
stemmer = nltk.stem.RSLPStemmer()

def limp_toks(toks):
    ns_toks = []
    for t in toks:
        nt = stemmer.stem(t.lower())
        if (2 < len(nt) < 30
            and re.match("^[a-z-]+", nt)
            and nt not in stopwords):
            ns_toks.append(nt)
    return ns_toks

q_tag = []
q_toks = []
for q in df.question:
    q = re.sub('[,".]', '', q)
    q = re.sub('[?;:]', '.', q
