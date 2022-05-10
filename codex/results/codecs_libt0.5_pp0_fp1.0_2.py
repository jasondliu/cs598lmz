import codecs
codecs.open('./data/prediction.txt', 'w', encoding='utf-8')

for i in range(len(prediction)):
    with codecs.open('./data/prediction.txt', 'a', encoding='utf-8') as f:
        f.write(str(prediction[i]) + '\n')

with codecs.open('./data/prediction.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
