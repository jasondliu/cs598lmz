import gc, weakref
from .resources import show_base_messages, base_messages
#from .errors import TatsuAlreadyParsed
from .errors import ParseException


##  Lexer
##
class Lexer(object):

    def __init__(self, grammar, whitespace='', trace=False,
                 encoding=None, semantics=None,
                 filename=None, ignorecase=False, debug=False):
        self.grammar = grammar
        self.whitespace = whitespace
        self.trace = trace
        self.encoding = encoding
        self.semantics = semantics
        self.filename = filename
        self.ignorecase = ignorecase
        self.debug = debug
        _prepare_regexp(self)
        return

    def parse(self, input, debug=False):
        (root, completed) = self.grammar.parse(input,
                                               whitespace=self.whitespace,
                                               trace=self.trace,
                                               filename=self.filename,
                                               encoding=self.encoding,
                                               semantics=self
