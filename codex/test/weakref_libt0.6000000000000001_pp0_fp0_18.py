import weakref
import xml.dom.minidom as minidom

from . import compat
from . import util

__all__ = ['load_file', 'load_string']


class _Element(object):
    def __init__(self, tag, attrib, text):
        self.tag = tag
        self.attrib = attrib
        self.text = text

    def __repr__(self):
        return '<%s %s %s>' % (self.tag, self.attrib, self.text)


class _ElementTree(object):
    def __init__(self):
        self._elements = []
        self._root = None

    def __repr__(self):
        return '<ElementTree %s>' % self._elements

    def getroot(self):
        return self._root

    def parse(self, filename):
        self._root = self._elements = load_file(filename)


def _convert_element(element):
    attrib = {}
