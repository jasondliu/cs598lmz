import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

filenames = [u'./data/tang/', u'./data/song/']
class PoetryModel:
    def __init__(self):
        self.model = None

    def load(self, file_path='poetry.model'):
        self.model = gensim.models.Word2Vec.load(file_path)

    def train(self, file_name, output_name='poetry.model', size=128, window=5, min_count=5, workers=4):
        sentences = PoetrySentence(file_name)
        self.model = gensim.models.Word2Vec(sentences, size=size, window=window, min_count=min_count, workers=workers)
        self.model.save(output_name)

    def vector_for(self, word):
        try:
            return self.model[word]
        except KeyError:
            return None

    def most_similar
