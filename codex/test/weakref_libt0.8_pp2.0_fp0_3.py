import weakref

from astroid import exceptions
from astroid.scoped_nodes import (
    ClassDef, FunctionDef, Lambda, Module,
    Param, With,
    )
from astroid.bases import (
    Instance, BoundMethod, Generator, GeneratorExit,
    StopIteration, BaseException,
    )
from astroid.exceptions import (
    InferenceError, NotFoundError,
    InferenceWarning, UnresolvableName,
    )
from astroid.brain import brain
from astroid.brain import builtins_lookup
from astroid.node_classes import (
    AssignAttr, AssignName, Assert, Assign,
    AugAssign, AugAssignAttr, Const, DelAttr,
    DelName, Delete, Exec, Expr, FunctionType,
    Import, ImportFrom, Index, keyword,
    Keyword, Subscript, Getattr, Call,
    Pass, Raise, Return, TryExcept, TryFinally,
    While, With, Yield,
    )
