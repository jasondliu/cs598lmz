import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import logging

from bs4 import BeautifulSoup as Soup
from bs4.element import NavigableString

from lily.base.constants import *
from lily.base.exception import ExceptionNotImplemented
from lily.base import validate

from lily.doc.factory import DocumentFactory
from lily.doc.document import Document
from lily.doc.drawing import Drawing
from lily.doc.text import Text
        
class Parser:

    def __init__(self, **kwords):
        """ Create a Lotus/Domino r4 to r8 Html parser. """
        
        self._parser = Soup(**kwords)
        self._parser.reset()
        
    def reset(self):
        """ Reset the parser. """
        self._parser.reset()
    
    def feed(self, data):
        """ Feed the parser with the html data. """
        self._parser.feed(data)
        return self._parser
        
    def close(
