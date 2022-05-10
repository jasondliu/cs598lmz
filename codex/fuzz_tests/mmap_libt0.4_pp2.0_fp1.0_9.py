import mmap
import os
import sys

from pygments.lexers import get_lexer_by_name
from pygments.token import Token
from pygments.util import ClassNotFound

from . import _compat as five
from . import _utils as utils
from . import _fileutils as fileutils
from . import _pygments_utils as pygments_utils
from . import _parser as parser
from . import _parser_utils as parser_utils


class File(object):
    """
    A file object.

    :param filename: The filename of the file.
    :param lexer: The lexer to use for the file.
    :param encoding: The encoding to use for the file.
    :param parser: The parser to use for the file.
    :param encoding: The encoding to use for the file.
    """

    def __init__(self, filename, lexer=None, parser=None, encoding=None):
        self.filename = filename
        self.lexer = lexer
        self.parser = parser
        self.encoding = encoding
        self.lines = None
