import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Model:
    def __init__(self, model_name, dir_path, embedding_dim, vocab_size, embedding_matrix, input_length, num_classes):
        self.model_name = model_name
        self.dir_path = dir_path
        self.embedding_dim = embedding_dim
        self.vocab_size = vocab_size
        self.embedding_matrix = embedding_matrix
        self.input_length = input_length
        self.num_classes = num_classes
        self.model = None
        self.kfold = None
        self.cvscores = []
        self.history = None
        self.tokenizer = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.X_train_glove = None
        self.X_test_glove
