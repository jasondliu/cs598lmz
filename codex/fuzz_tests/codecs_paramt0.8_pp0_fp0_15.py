import codecs
codecs.register_error('strict', codecs.ignore_errors)

outfile = codecs.open('normalized.txt', 'w+', 'utf-8')
with codecs.open('raw.txt', 'r', 'utf-8') as f:
    for line in f:
        line = line.lower()
        line = line.strip('\n')
        line = line.strip()
        outfile.write(line)
        outfile.write('\n')
outfile.close()

with open('normalized.txt') as f:
    corpus = f.read()

# evaluate loaded model on test data
loaded_model = Word2Vec.load('./model.bin')
print(loaded_model)

print(loaded_model['facebook'])
# print(loaded_model.similarity('facebook', 'twitter'))
# print(loaded_model.most_similar(positive=['women', 'king'], negative=['man']))

# remove stop words
stop_words = set(stopwords.words('english'))
stop_words.update(['.'
