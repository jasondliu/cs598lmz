import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def read_file(path):
    """Read a file from a path.

    Args:
        path: path to a file.

    Returns:
        The text in the file.
    """
    with path.open(encoding='utf-8', errors='replace_with_space') as f:
        return f.read()


def preprocess_file(file_contents, vocab_size):
    """Preprocess a single file.

    Args:
        file_contents: string, contents of a file
        vocab_size: integer, number of words in the vocabulary

    Returns:
        A list of integers representing the words in the file.
    """
    file_contents = re.sub("[^a-zA-Z]", " ", file_contents)
    file_contents = file_contents.lower()
    file_contents = file_contents.split()

    file_contents = [w for w in file_contents if len(w
