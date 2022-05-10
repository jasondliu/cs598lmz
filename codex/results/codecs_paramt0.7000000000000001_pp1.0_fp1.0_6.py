import codecs
codecs.register_error('strict', codecs.ignore_errors)

from collections import namedtuple

from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight

from hunor.common.config import Options
from hunor.common import regex

from hunor.parse.parser import Parser
from hunor.parse.state import State
from hunor.parse.factory import ParserFactory
from hunor.parse.token import Token

from hunor.parse.visitor import Visitor
from hunor.parse.visitor import NodeVisitor


#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------

def walk(node):
    visitor = NodeVisitor()
    visitor.visit(node)

def print_tree(node):
    print(node)
    for child in node.children:
        print_tree(child)

def print_node(node, name, indent):
    print(indent + str(name))
    for child
