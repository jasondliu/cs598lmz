import bz2
bz2.__version__

import scipy
scipy.__version__

import sklearn
sklearn.__version__

import nltk
nltk.__version__

path_corpus_raw = 'E:/Kyk_Projeler/2_Sentiment_Analysis_of_Comments/datasets/comments/all/comments.csv'
path_corpus_processed = 'E:/Kyk_Projeler/2_Sentiment_Analysis_of_Comments/datasets/comments/all/comments_processed.txt'
path_vocab = 'E:/Kyk_Projeler/2_Sentiment_Analysis_of_Comments/datasets/comments/all/vocab.txt'
data = []
with open(path_corpus_raw,'r',encoding='utf-8') as corpus:
    i=0
    while i < 20000:
        data.append(corpus.readline().split(';')[-2])
        i+=1
print(data[:10])

len(
