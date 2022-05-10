import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data(path):
    with codecs.open(path, 'r', 'utf-8', 'replace_with_space') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]   # header 제외
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

from konlpy.tag import Okt
pos_tagger = Okt()

def tokenize(doc):
    # norm, stem은 optional
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json') as f:
        train_docs = json.load(f)
    with open('test_docs.json') as f:

