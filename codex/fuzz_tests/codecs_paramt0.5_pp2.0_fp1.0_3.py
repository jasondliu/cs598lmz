import codecs
codecs.register_error('ignore_surrogates', codecs.lookup_error('ignore'))

def read_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore_surrogates') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
    return data

train_data = read_data('../data/ratings_train.txt')
test_data = read_data('../data/ratings_test.txt')

from konlpy.tag import Twitter
pos_tagger = Twitter()

# 문장의 형태소 분석 결과를 담을 리스트 생성
def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타
