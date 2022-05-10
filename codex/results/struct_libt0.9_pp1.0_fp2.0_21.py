import _struct

from .. import exceptions
from .. import q
from .. import types as t
from .. import macros as m
from .. import util as u
from ..session import Session

from ..atoms.numbers import Number
from ..atoms.pair import Pair
from ..atoms.t import T
from ..atoms.nil import Nil
from ..atoms.symbol import Symbol
from ..atoms.function import Function, Expander, Macro

from .objects import Object

#: The size of one character in bits
CHAR_BITS = 8


@q.as_q("character")
def char(code: t.Number, encoding="utf-8") -> (t.Char, t.Str):
    """
    Converts the given unicode code point character to a single character string.
    """
    # TODO: Add more encodings?
    assert encoding in {"utf-8", "ascii"}
    code = int(code)
    return code, code.to_bytes(1, "big").decode(encoding)


@q.func_objects.add(q.
