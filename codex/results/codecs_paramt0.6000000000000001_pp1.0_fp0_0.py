import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ------------------------------------------------------------------------------

class HtmlParser(HTMLParser):
    """
    Parser for HTML documents.
    """
    def __init__(self):
        HTMLParser.__init__(self)

        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

# ------------------------------------------------------------------------------

class HtmlFinder(object):
    """
    Finder for HTML documents.
    """
    def __init__(self, root):
        self.root = root

    def find(self, ext):
        """
        Returns a list of absolute pathnames of files of the given extension.
        """
        files = []

        for root, dirs, files in os.walk(self.root):
            for f in files:
                if os.path.splitext(f)[1] == ext:
                    files.append(os.
