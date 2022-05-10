import types
types.SimpleNamespace = types.ModuleType('SimpleNamespace', ' ')

from collections import OrderedDict
import ast
from importlib import import_module
import inspect
import logging
import sys
from .VERSION import version_info
from .loggers import new_logger

__version__ = '.'.join([str(v) for v in version_info])

logger = new_logger('kutils.import_util')

