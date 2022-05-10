import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def read_files(files, encoding="cp65001"):
    """Read files into dataset as a list of rows."""
    data = []
    for filename in files:
        with codecs.open(filename, "r", encoding=encoding) as f:
            data.extend(f.read().splitlines())
    return data

def load_dataset(path, **kwargs):
    """Load dataset (training set and test set) from files."""
    train_file = os.path.join(path, 'train.txt')
    test_file = os.path.join(path, 'test.txt')
    encoding = kwargs.pop('encoding', "cp65001")

    train_data = read_files([train_file], encoding=encoding)
    test_data = read_files([test_file], encoding=encoding)
    return (train_data, test_data)

def get_labels(data):
