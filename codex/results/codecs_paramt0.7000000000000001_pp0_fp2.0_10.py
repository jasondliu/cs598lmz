import codecs
codecs.register_error('strict', codecs.ignore_errors)

class ChatterBotCorpusTrainer(Trainer):
    """
    Allows the chat bot to be trained using data from the
    ChatterBot dialog corpus.
    """

    def __init__(self, storage, **kwargs):
        super(ChatterBotCorpusTrainer, self).__init__(storage, **kwargs)

    def train(self, *corpus_paths):
        """
        Train the chat bot based on the data in the specified corpus.
        """
        for corpus_path in corpus_paths:
            self.train_corpus(corpus_path)

    def train_corpus(self, corpus_path):
        """
        Train the chat bot based on the data in the specified corpus.
        """
        lines = self.get_lines(corpus_path)

        for line in lines:
            line = line.strip()

            # Ignore blank lines
            if not line:
                continue

            statement = Statement(line)

            self.storage.create(statement)


