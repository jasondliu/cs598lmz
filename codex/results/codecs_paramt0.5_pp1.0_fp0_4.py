import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def read_file(path):
    """
    Reads a file and returns a list of words.
    """
    with codecs.open(path, 'r', 'utf-8', 'replace_with_space') as f:
        document = f.read()
        document = document.replace('\n', ' ')
        document = document.replace('\r', ' ')
        document = document.replace('\t', ' ')
        document = document.replace('\xa0', ' ')
        document = document.replace('\u2022', ' ')
        document = document.replace('\u2026', ' ')
        document = document.replace('\u2013', ' ')
        document = document.replace('\u2014', ' ')
        document = document.replace('\u2018', ' ')
        document = document.replace('\u2019', ' ')
        document = document.replace('\u201c', ' ')
        document = document.replace
