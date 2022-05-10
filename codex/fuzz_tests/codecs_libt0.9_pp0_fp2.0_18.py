import codecs
codecs.open


def uconv(text):
    return text.decode('utf8')


def preProcess(text):
    text = uconv(text)
    text = lang.preProcess(text)
    return text

def cleanHTML(text):
    text = uconv(text)
    
    OPENING_TAG = re.compile(r'<[^>]*>')
    CLOSING_TAG = re.compile(r'</[^>]*>')
    
    while len(text) > 0:
        match = OPENING_TAG.search(text)
        if match:
            text = text[:match.start()] + text[match.end():]
        match = CLOSING_TAG.search(text)
        if match:
            text = text[:match.start()] + text[match.end():]
        else:
            break
    
    return text
    
class FileIterator:
    def __init__(self, filein):
        self.fileobj = file(filein, 'r')

    def __
