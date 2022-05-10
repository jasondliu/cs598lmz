import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.tags = []
        self.words = []
        self.tag_to_idx = {}
        self.word_to_idx = {}
        self.max_len = 0
        self.load_data()

    def load_data(self):
        with codecs.open(self.filename, 'r', 'utf-8', 'replace_with_space') as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                word, tag = line.split("\t")
                self.data.append([word, tag])
                if tag not in self.tag_to_idx:
                    self.tag_to_idx[tag] = len(self.tag_to_idx)
                    self.tags.append(tag)
                if word not in self.word_to_idx:

