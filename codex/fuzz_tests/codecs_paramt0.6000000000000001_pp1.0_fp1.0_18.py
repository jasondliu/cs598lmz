import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def load_data(filename, max_length=None, length_from=False):
    with codecs.open(filename, encoding="utf8") as f:
        return f.read().splitlines()

def load_dataset(dataset_path):
    train_data = load_data(os.path.join(dataset_path, 'train.txt'))
    valid_data = load_data(os.path.join(dataset_path, 'valid.txt'))
    test_data = load_data(os.path.join(dataset_path, 'test.txt'))
    return train_data, valid_data, test_data

def _tokenize(sentence, tokenizer):
    words = tokenizer.tokenize(sentence)
    return words

def tokenize(sentence, tokenizer):
    words = _tokenize(sentence, tokenizer)
    return ' '.join(words)

def batch_tokenize(sentences, tokenizer):
    return [token
