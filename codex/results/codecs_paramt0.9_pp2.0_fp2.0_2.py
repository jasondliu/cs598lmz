import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
if PYTHON_VERSION < 3:
    _py3 = False
else:
    _py3 = True

#types
if not _py3:
    long = long
    unicode = unicode
    str = str
    bytes = str
    int = int
    NoneType = types.NoneType
    bool = types.BooleanType
    from types import DictType
    from types import TupleType
    from types import ListType
    from types import StringTypes
    from types import StringType
    StringType = StringTypes[0]
else:
    long = int
    unicode = str
    str = str
    bytes = bytes
    int = int
    NoneType = type(None)
    from types import MethodType
    from types import LambdaType
    from types import FunctionType
    from types import BuiltinFunctionType
    from types import BuiltinMethodType
    from types import GeneratorType
    bool = bool
    DictType = dict
    TupleType = tuple
    ListType = list
