import weakref
from contextlib import contextmanager
from functools import partial
from itertools import count
from typing import Optional, List, Dict, Any, Tuple, Callable, TypeVar, Type, Set, Iterable, Union, Iterator, TextIO

from . import util, settings, exceptions, types, marshal, ast, scope, lexer, parser
