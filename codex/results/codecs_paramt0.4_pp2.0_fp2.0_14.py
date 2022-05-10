import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='strict') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]   # header 제외
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

# 영화 리뷰 문장 처리
def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
