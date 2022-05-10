import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
            yield dictionary.doc2bow(line.lower().split())

class MyCorpus_2(object):
    def __iter__(self):
        for line in open('mycorpus_2.txt'):
            yield dictionary.doc2bow(line.lower().split())

# remove words that appear only once
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids)  # remove stop words and words that appear only once
dictionary.compactify()  # remove gaps in id sequence after words that were removed
print dictionary

# get the corpus
corpus = MyCorpus()
corpus_2 = MyCorpus_2()

# save the dictionary and corpus for future use
dictionary.save('/tmp/
