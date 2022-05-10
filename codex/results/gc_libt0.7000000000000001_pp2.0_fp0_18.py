import gc, weakref
import functools

from sympy.core.compatibility import is_sequence
from sympy.core.containers import Tuple, Dict
from sympy.core.decorators import deprecated
from sympy.core.basic import Basic
from sympy.core.symbol import Symbol, Dummy
from sympy.core.singleton import Singleton, S
from sympy.core.sympify import _sympify, sympify
from sympy.core.sympify import converter
from sympy.core.sympify import SympifyError
from sympy.core.cache import cacheit
from sympy.core.compatibility import string_types, range, with_metaclass
from sympy.core.expr import Expr
from sympy.core.symbols import Wild, Symbol, Dummy, symbols
from sympy.core.numbers import Rational
from sympy.core.function import Function, Derivative
from sympy.core.power import Pow
from sympy.utilities.exceptions import SymPyDeprecationWarning
from sympy.utilities.misc import fillded
