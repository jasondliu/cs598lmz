import codecs
codecs.register_error('strict', codecs.ignore_errors)

# we'll use utf-8 encoding for everything
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


# the dataset is a list of pairs, each consisting of a word and
# a list of its neighbors, like ('dog', ['the', 'a']).
dataset = []

# load up the brown corpus, if it's not already loaded
try:
    dataset = nltk.data.load('../data/br-sentences.pickle')
except LookupError:
    from nltk.corpus import brown

    # process each of the genre files
    for genre in brown.categories():
        for fileid in brown.fileids(genre):
            sentence_list = brown.sents(fileid)
            for sentence in sentence_list:
                # go through each word in the sentence
                for i in xrange(len(sentence)):
                    word = sentence[i]
                    # associate it with its neighboring words
                    neighbors = sentence[
