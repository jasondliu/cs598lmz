import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(dirname, fname):
    """
    Read file contents and split into lines.
    Args:
        dirname(str): The path of the data directory.
        fname(str): The filename.
    Returns:
        list(str): The data, split into lines.
    Raises:
        IOError: If the file doesn't exist.
    """
    fname = os.path.join(dirname, fname)

    if os.path.exists(fname):
        with codecs.open(fname, "r", "utf-8", "ignore") as f:
            return f.read().strip().split("\n")
    else:
        raise IOError("Unable to open file", fname)


def get_dialogue_lines(fname, lines):
    """
    Iterate through the lines of the file, and separate them into conversations.
    """
    id2line = {}
    convs = []
    with codecs.open(fname, "r",
