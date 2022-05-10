import codecs
codecs.register_error('ignore_invalid_xmlchars', codecs.ignore_errors)

class ImportError(Exception):
    pass

class Import(object):
    def __init__(self, file):
        self.file = file
        self.xml = codecs.open(file, 'r', encoding='utf-8', errors='ignore_invalid_xmlchars').read()
        self.tree = etree.parse(StringIO(self.xml))
        self.root = self.tree.getroot()

    def _get_elements(self, tag):
        return self.root.findall(tag)

    def _get_element(self, tag):
        return self.root.find(tag)

    def _get_element_text(self, tag):
        return self._get_element(tag).text

    def _get_element_attr(self, tag, attr):
        return self._get_element(tag).get(attr)

    def _get_element_int(self, tag):
        return int(self._get_element_text(tag))

   
