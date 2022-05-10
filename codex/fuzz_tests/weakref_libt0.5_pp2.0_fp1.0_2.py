import weakref
from contextlib import contextmanager
from functools import partial
from itertools import count
from typing import Optional, List, Dict, Any, Tuple, Callable, TypeVar, Type, Set, Iterable, Union, Iterator, TextIO

from . import util, settings, exceptions, types, marshal, ast, scope, lexer, parser
from .ast import Node, Function, Class, ClassMethod, InstanceMethod, Property, PropertyGetter, PropertySetter, Yield, \
    YieldFrom, Await, AwaitFrom, Call, Import, ImportFrom, Decorator, DecoratorCall, Lambda, Return, Raise, \
    For, While, Break, Continue, If, Assign, Delete, Global, NonLocal, Assert, Pass, Try, With, Const, Attribute, \
    Subscript, Slice, Index, ListComp, SetComp, DictComp, GeneratorExp, Tuple, List, Set, Dict, Name, Num, Str, \
    Bytes, Ellipsis, BoolOp, BinOp, UnaryOp, Compare, And, Or, Not,
