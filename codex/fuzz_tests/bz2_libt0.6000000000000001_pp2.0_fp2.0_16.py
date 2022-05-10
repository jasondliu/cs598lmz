import bz2
bz2.BZ2File('./data/wiki.txt.bz2')

with bz2.BZ2File('./data/wiki.txt.bz2') as f:
    for i in range(5):
        print(f.readline())

# バイナリファイルを読む
import pickle
with open('./data/pickle.bin', 'rb') as f:
    data = pickle.load(f)
    print(data)

# テキストファイルを読む
with open('./data/text.txt', 'rt') as f:
    for line in f:
        print(line.strip())

# 文字コードを指定して読む
with open('./data/text.txt', 'rt', encoding='utf-8') as f:
    print(f.read())

# 文字コードを推測して読む
with open('./data/text
