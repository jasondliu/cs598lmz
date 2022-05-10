import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()
        data = data.replace(u'\ufeff', '')
        data = data.replace(u'\u3000', '')
        return data

def tokenize(sent):
    '''Return the tokens of a sentence including punctuation.
    >>> tokenize('Bob dropped the apple. Where is the apple?')
    ['Bob', 'dropped', 'the', 'apple', '.', 'Where', 'is', 'the', 'apple', '?']
    '''
    return [x.strip() for x in re.split('(\W+)?', sent) if x.strip()]

def parse_stories(lines, only_supporting=False):
    '''Parse stories provided in the bAbi tasks format
    If only_supporting is true, only the sentences that support the answer are kept.

