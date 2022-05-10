import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.models import Word2Vec

# load up unzipped corpus from http://mattmahoney.net/dc/text8.zip
sentences = gensim.models.word2vec.Text8Corpus('text8')

# train the skip-gram model; default window=5
model = Word2Vec(sentences, size=200)

# ... and some hours later... just as advertised...
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

# pickle the entire model to disk, so we can load&resume training later
model.save(os.path.join('/tmp', 'text8.model'))
# store the
