import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# Load the pre-trained model

class PreTrainedModel(object):

    def __init__(self, model_path, dim):
        """
        Prepare model
        :param model_path: path to the pre-trained model, can be either with or without '.bin' extension
        :param dim: dimension of the model
        """
        self.model_path = model_path
        trim_rule = re.compile('[^a-z0-9а-яё]')

        self.dim = dim

        if os.path.isfile(model_path):
            model = KeyedVectors.load_word2vec_format(model_path, binary=True)
        else:
            model = KeyedVectors.load_word2vec_format(model_path + '.bin', binary=True)

        self.model = model

    def __getitem__(self, word):
        """
        Return vector representation of the `word`.
        :param word: string
