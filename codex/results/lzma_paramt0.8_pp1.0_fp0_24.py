from lzma import LZMADecompressor
LZMADecompressor

from gensim import corpora
dictionary = corpora.Dictionary.load('/Users/mai/Desktop/Courses/GLML/project/output/dict.txt')
#dictionary.filter_extremes(no_below=5, no_above=0.5)
#dictionary.compactify()
#dictionary.save('/Users/mai/Desktop/Courses/GLML/project/output/dict3.txt')

from gensim.models import TfidfModel
tfidf = TfidfModel.load('/Users/mai/Desktop/Courses/GLML/project/output/tfidf.txt')

from gensim.models import LsiModel
lsi = LsiModel.load('/Users/mai/Desktop/Courses/GLML/project/output/lsi.txt')

from gensim.models import LdaModel
lda = LdaModel.load('/Users/mai/Desktop/Courses/GLML/project/output/lda.txt')

#from gensim.models import
