from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("./data/train.ft.txt.bz2", "rb").read())

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
train.head()

#preprocessing
train['text'] = train['text'].apply(lambda x: x.lower())
train['text'] = train['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

test['text'] = test['text'].apply(lambda x: x.lower())
test['text'] = test['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

#tokenization
tokenized_train = train['text'].apply(lambda x: x.split())
tokenized_test = test['
