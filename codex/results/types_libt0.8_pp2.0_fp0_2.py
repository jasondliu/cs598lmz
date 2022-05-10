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


def import_from_fpath(package_fpath, component, component_name=None):
    """
    Import component from a file to be defined in kutils specific package:
    ``package_fpath``
    The package directory must have an ``__init__.py`` file.

    The component of interest must be a Python class as specified by
    ``component``. This class must be defined in the imported file.

    If the component of interest does not have a name, then ``component_name``
    should be specified, or else, the name of the component will be inferred
    from the name of the file in which the component is defined minus the
    extension ``
