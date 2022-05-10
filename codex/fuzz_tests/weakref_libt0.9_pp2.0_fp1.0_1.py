import weakref
from ply import yacc

from tatsu.util import asjson
from tatsu.codegen import MetaContext
from tatsu.codegen import CodeGenerator
from tatsu.codegen import CodeWriter
from tatsu.util import deferred, defaultdict
from tatsu.walkers import NodeWalker, Walker
from tatsu.walkers import WalkerRegistry
from tatsu.assembler import Assembler
from tatsu.assembler import InlineAssembler
from tatsu.errors import FailedParse, FailedSemantics

from .semantics import DefaultSemantics, SemanticsRegistry, CallSemantics
from .compat import io
from .ast import AST
from .ast import reduce_ebnf_ast
from .errors import FailedTokenization
from .errors import FailedConversion
from .errors import FailedCompilation
from .enfa import E_NFA
from .enfa import EOFAction
from .enfa import Precedence
from .dfa import DFA
from .grammar import Grammar


def _set_default(settings, k, default):
    if default & settings[k]:
