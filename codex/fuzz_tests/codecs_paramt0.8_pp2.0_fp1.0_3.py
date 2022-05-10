import codecs
codecs.register_error('drop', drop)

#read file in as a single string
#filename = 'HarryPotterandthePhilosophersStone.txt'
filename = 'poem.txt'
data_source = 'speedy' if filename == 'poem.txt' else 'source'
s = ''
with open(filename) as f:
    for line in f:
        s += line.strip()

#find unique characters in the string
#convert to list
chars = sorted(list(set(s)))
print 'total chars:', len(chars)
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

#cut the text in semi-redundant sequences of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(s) - maxlen, step):
    sentences.append(s[i: i + maxlen])
    next_chars.append(
