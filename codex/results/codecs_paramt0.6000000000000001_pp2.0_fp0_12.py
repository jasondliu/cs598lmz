import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

class DataReader(object):
    def __init__(self, folder_dir, vocab_file, file_name_list):
        self.folder_dir = folder_dir
        self.vocab_file = vocab_file
        self.file_name_list = file_name_list

    def read_vocab(self):
        with codecs.open(self.vocab_file, 'r', 'utf-8') as f:
            vocab = [line.strip() for line in f]
        return vocab

    def read_raw_data(self, file_name):
        with codecs.open(os.path.join(self.folder_dir, file_name), 'r', 'utf-8', errors='surrogate_or_strict') as f:
            raw_data = [line.strip() for line in f]
        return raw_data

    def read_raw_data_list(self):
        raw_data_list = []
        for file_name
