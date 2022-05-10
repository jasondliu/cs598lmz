import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))


class Category:

    def __init__(self, name, keywords=[], phrases=[]):
        self.name = name
        self.keywords = keywords
        self.phrases = phrases


def load_categories(filename):
    """
    Load from a file the list of categories
    """

    categories = []

    with codecs.open(filename, encoding='utf8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            (name, keywords, phrases) = line.strip().split('\t')
            categories.append(Category(name, keywords.split(','), phrases.split(',')))
    return categories


class Feature:
    """
    Simple class to hold feature-related info.
    """

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __hash__(self):
        return hash(self.type + self.value)

    def __eq__(
