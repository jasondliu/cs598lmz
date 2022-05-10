import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

# train set 1

f = codecs.open('./dataset/crf/TrainSet1.txt', encoding='utf-8', errors='replace_with_space')

sents = f.read().split('\n')

sents = [s.split() for s in sents if s]

for i, s in enumerate(sents):
    for j, w in enumerate(s):
        s[j] = w+"\tB"
    sents[i] = '\n'.join(s)

with open("dataset/crf/TrainSet1.txt", "w") as f:
    f.writelines(['%s\n' % s for s in sents])
