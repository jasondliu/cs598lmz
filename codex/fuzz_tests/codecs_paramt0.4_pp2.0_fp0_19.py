import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

class MyCorpus2(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

def get_corpus_from_file(filename):
    mycorpus = []
    for line in open(filename):
        # assume there's one document per line, tokens separated by whitespace
        mycorpus.append(line.lower().split())
    return mycorpus

def get_corpus_from_file2(filename):
    mycorpus = []
    for line in open(filename):
        # assume there's one document
