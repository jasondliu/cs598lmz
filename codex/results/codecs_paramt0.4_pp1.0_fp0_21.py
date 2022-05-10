import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_paths(path):
    """
    Get the paths of all files in a directory and its subdirectories.
    """
    paths = []
    for root, dirs, files in os.walk(path):
        for f in files:
            paths.append(os.path.join(root, f))
    return paths


def get_text(path):
    """
    Get the text of a file.
    """
    with codecs.open(path, 'r', encoding='utf-8', errors='strict') as f:
        text = f.read()
    return text


def get_texts(path):
    """
    Get the texts of all files in a directory and its subdirectories.
    """
    paths = get_paths(path)
    texts = []
    for path in paths:
        text = get_text(path)
        texts.append(text)
    return texts


def get_texts_by_dir(path):
    """
    Get the texts of
