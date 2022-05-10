import codecs
codecs.register_error('ignore_exceptions', codecs.ignore_errors)

class Batch:
    def __init__(self, source, target_input, target_output=None, source_length=None, target_length=None):
        self.source = source
        self.target_input = target_input
        self.target_output = target_output if target_output is not None else target_input
        self.source_length = source_length if source_length is not None else np.ones(len(source), dtype='int32')
        self.target_length = target_length if target_length is not None else np.ones(len(target_input), dtype='int32')

def read_corpus(filename, max_size=None):
    data = []
    with codecs.open(filename, encoding='utf-8') as f:
        for line in f:
            tokens = line.strip().split()
            data.append(tokens)
            if max_size and len(data) >= max_size:
                break
    return data

def build_
