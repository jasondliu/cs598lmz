import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)  # Python 2

def _load_data(data_path, label_path):
    """Loads data from files, splits the data into words and generates labels.

    Args:
        data_path: path to the file containing data
        label_path: path to the file containing labels

    Returns:
        tuple of (sentences, labels)
    """
    x_text = []
    y = []
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            x_text.append(line.strip())
    with open(label_path, 'r', encoding='utf-8') as f:
        for line in f:
            y.append(int(line.strip()))

    return x_text, y

def load_data():
    """Loads and preprocessed data for the dataset.

    Returns:
        tuple of (sentences, labels)
    """
    # Load data from files
    x_text, y = _load
