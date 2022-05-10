import types
types.ModuleType.__getattr__ = lambda self, key: lambda *args, **kwargs: self.__getattribute__(key)(*args, **kwargs)
'''

import os

# pylint: disable=unused-import
# pylint: disable=wrong-import-position

import _thread
import builtins
import encryption
import gc
import tokenizer
import ast
import operator
import _codecs
import unittest
import tempfile


# pylint: disable=no-member, incorrect-string-conversion
# pylint: disable=invalid-name, too-many-locals, unused-argument
# pylint: disable=too-many-branches, too-many-statements
# pylint: disable=consider-iterating-dictionary


# pylint: disable=too-many-nested-blocks


# pylint: disable=too-many-instance-attributes


def is_py3():
    return sys.version_info[0] == 3


def is_py2():
    return
