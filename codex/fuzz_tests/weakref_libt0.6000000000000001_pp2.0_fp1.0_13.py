import weakref

from .. import data
from .. import tools
from .. import types

from ..data import convert

from ..tools import (
    clsname,
    indent,
    is_empty,
    is_list_like,
    is_sequence,
    strip_control_sequences,
    uniq,
    )

from ..types import (
    is_bytes,
    is_collection,
    is_dict,
    is_integer,
    is_list,
    is_string,
    is_type,
    is_tuple,
    )

from . import (
    constants,
    errors,
    )

from .comments import Comments
from .constants import (
    BINARY_OPERATORS,
    BLOCK_STATEMENTS,
    COMMENT_MARKERS,
    COMPARISON_OPERATORS,
    EXPRESSION_STATEMENTS,
    KEYWORDS,
    LITERALS,
    LINE_STATEMENTS,
    LOGICAL_OPERATORS,
    LOOP_STATEMENTS,

