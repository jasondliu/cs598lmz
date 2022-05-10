import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class UnicodeHandler():
    """
    Unicode handler class.
    Detects text encoding and converts to UTF-8
    """

    def __init__(self):
        """
        """

    def convert(self, text):
        """
        @text - String with text to be converted
        """
        try:
            text = text.decode("utf-8")
        except:
            try:
                text = text.decode("latin-1")
            except:
                pass
            else:
                pass
        return text.encode("utf-8")

def get_doc(path):
    f = open(path, 'r')
    html = f.read()
    f.close()
    return html

def get_html(link):
    """
    @link - a link to the website
    """
    try:
        req = urllib2.Request(link, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21
