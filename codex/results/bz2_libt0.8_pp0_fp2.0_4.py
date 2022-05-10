import bz2
bz2_data = bz2.BZ2File('data/extracted/vocab.bz2', 'rb')
vocab = pickle.load(bz2_data)
bz2_data.close()

# len(vocab)
# type(vocab)

# vocab
# vocab[:10]

# vocab[0]
# type(vocab[0])


print(len(vocab))
print('%s ... %s' % (vocab[0], vocab[-1]))
print(' '.join(vocab[0:10]))

# vocab.index('wife')

# vocab[37847]

# vocab.count('NO')

# vocab.count('<unk>')

# vocab.count('the')

# for i in range(100):
#     vocab.count(vocab[i])

# for i in range(10, 20):
#     freq = vocab.count(vocab[i])
#     print('%s: %s times
