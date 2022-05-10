import types
types.SimpleNamespace

import itertools

from collections import OrderedDict
from typing import List, Tuple, Dict, Set, Union
from typing_extensions import Final

from mypy.nodes import (
    ARG_POS, ARG_NAMED, ARG_STAR, ARG_STAR2, ARG_OPT, ARG_NAMED_OPT, TypeInfo, FuncDef,
    OverloadedFuncDef, Block, MypyFile, TypeVarDef, Var, LDEF, MDEF, GDEF,
    Decorator, Expression, NameExpr, RefExpr, MemberExpr, FuncDef,
    CallExpr, ClassDef, Var, AssignmentStmt, OpExpr, UnaryExpr, IndexExpr,
    ListExpr, TupleExpr, SetExpr, DictionaryExpr, Context, StrExpr, BytesExpr,
    UnicodeExpr, IntExpr, FloatExpr, ComplexExpr, EllipsisExpr, StarExpr,
    YieldFromExpr, YieldExpr, TypeApplication, Super
