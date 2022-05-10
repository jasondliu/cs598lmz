import codecs
codecs.register_error('surrogatepass', codecs.recodec_error)

def normalize(string, lang='en'):
    """Normalizes the string by converting it to Unicode."""
    #if not isinstance(string, unicode):
    #    string = string.decode('utf-8')
    return unicodedata.normalize('NFC', string)


def normalize_line(string, lang='en'):
    """Normalizes the string by converting it to Unicode."""
    string = normalize(string)
    return string.strip()


def read_lines(filepath, lang='en'):
    """Reads all lines from a file."""
    with codecs.open(filepath, 'rb', 'utf-8', errors='surrogatepass') as f:
        lines = f.readlines()
    return [normalize_line(l) for l in lines if l.strip()]


def read_lines_from_list(filepaths, lang='en'):
    """Reads all lines from a list of files."""
    lines = []

