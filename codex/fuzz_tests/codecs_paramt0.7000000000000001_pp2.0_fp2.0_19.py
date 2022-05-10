import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
 
class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())
 
class MyCorpus1(object):
    def __iter__(self):
        for line in open('mycorpus1.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())
 
corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
corpus_memory_friendly1 = MyCorpus1() # doesn't load the corpus into memory!
print(corpus_memory_friendly)
print(corpus_memory_friendly1)
 
#for vector in corpus_memory_friendly: # load one vector into memory at a time
#    print(vector)
 
#corpus =
