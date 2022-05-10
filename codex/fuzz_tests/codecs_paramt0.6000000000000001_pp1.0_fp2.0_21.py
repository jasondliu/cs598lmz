import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_insults(path):
    """
    Parse the insults from the given path.
    """
    with codecs.open(path, "r", "utf-8", "ignore") as f:
        for line in f:
            yield unicode(line.strip().lower())

def get_insults():
    """
    Get a list of insults.
    """
    return list(parse_insults(os.path.join(os.path.dirname(__file__), "insults.txt")))
