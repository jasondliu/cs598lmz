import weakref
from collections import defaultdict

import numpy as np
import six
import tensorflow as tf

from . import core
from . import functional as F
from . import layers
from . import variables as V
from ..utils import auto_reuse
from ..utils import get_scope_name


def _get_default_scope_name(shape, name):
    if isinstance(name, six.string_types):
        return name
    default_name = "output_shape"
    if len(shape) == 1:
        return default_name
    else:
        return "%s_%s" % (default_name, len(shape))


class _OutputShape(object):
    _scope_name = ""
    _scope_shape = None
    _scope_shape_name = None

    def __init__(self, shape, name=None):
        self._scope_shape = shape
        self._scope_name = _get_default_scope_name(shape, name)
        self._scope_shape_name = "%s_shape" % self._scope_name
