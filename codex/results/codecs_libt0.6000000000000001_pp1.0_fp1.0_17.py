import codecs
codecs.open('', encoding='utf-8')

def read_data(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]   # header 제외
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')
from konlpy.tag import Okt

# Okt: Open Korean Text
okt = Okt()

# 트위터 형태소 분석기
# okt = Okt()
# okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)

# 예시
# ['아버지/
