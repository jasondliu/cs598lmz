import codecs
codecs.register_error('ignore', codecs.ignore_errors)

from multiprocessing import Pool

from gensim.models import word2vec


def get_sentences(filename):
    sentences = []
    with open(filename, 'r') as f:
        for line in f:
            sentences.append(line.split())
    return sentences


def train(filename):
    sentences = get_sentences(filename)
    model = word2vec.Word2Vec(sentences, size=300, min_count=1, window=5, iter=10)
    model.save(filename + '.model')


def train_all():
    filenames = ['train_pos.txt', 'train_neg.txt', 'test_pos.txt', 'test_neg.txt']
    pool = Pool(processes=4)
    pool.map(train, filenames)


def load_model(filename):
    return word2vec.Word2Vec.load(filename)


def get_vectors(model):
    vectors = []
    for word in model.vocab
