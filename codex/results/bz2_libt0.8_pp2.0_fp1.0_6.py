import bz2
bz2_data = bz2.BZ2File('../data/train.ft.txt.bz2')
lines = [x.decode('utf-8') for x in bz2_data.readlines()]
lines = lines[8:]

docs = []

for line in lines:
    arr = line.split('\t')

    if len(arr) != 2:
        continue

    _id = arr[0]
    review = arr[1].strip()

    docs.append((_id, review))

print('Number of documents:', len(docs))

# 전처리


def preprocess(review):
    """
    전처리 함수
    :param review: 리뷰 문자열
    :return: 전처리된 리뷰 문자열
    """
    try:
        # 소문자로 변
