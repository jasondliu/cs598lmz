from types import FunctionType
list(FunctionType('sin', 0, 0, 1, None, None, 'l', '', '', 0, None))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from inspect import signature, Parameter
from typing import TypeVar, Generic, Callable, List, Union, Tuple

T_repr = TypeVar('T_repr')  # noqa


def func_from_signature(sig: signature) -> Callable:
    """
    from stubs.pyi
    """
    code = "def f{0}: return None".format(sig)
    namespace = {}
    exec(code, namespace, namespace)  # type: ignore
    return namespace['f']  # type: ignore


def arg_names(params: List[Parameter]) -> List[str]:
    return [param.name for param in params]


class TypedFunction:
    def __init__(self, base_function: Callable, *args, **kwargs):
        self._base_function = base_function
        self.args = args

