import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

from . import pure
from .pure import parse
from .pure import ParserError
from .pure import ParseError
from .pure import PrinterError
from .pure import PrintError
from .pure import WriteError
from .pure import SyntaxError
from .pure import MissingArgumentError
from .pure import OverloadedMethodNameError
from .pure impo
