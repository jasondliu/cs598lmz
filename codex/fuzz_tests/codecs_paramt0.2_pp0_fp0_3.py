import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load the corpus
logging.info('Loading corpus')
corpus = corpora.MmCorpus('corpus.mm')

# Load the dictionary
logging.info('Loading dictionary')
dictionary = corpora.Dictionary.load('dictionary.dict')

# Load the LDA model
logging.info('Loading LDA model')
lda = models.LdaModel.load('lda.model')

# Load the TF-IDF model
logging.info('Loading TF-IDF model')
tfidf = models.TfidfModel.load('tfidf.model')

# Load the index
logging.info('Loading index')
index = similarities.MatrixSimilarity.load('index.index')

# Load the stopwords
logging.info('Loading stopwords')
stopwords = set(nltk.cor
