import weakref
from xml.etree import ElementTree
from xml.sax import saxutils

from jsonpath_ng import parse
from jsonpath_ng.ext import parse as jsonpath_parse

from . import constants
from .exceptions import (
    JSONPathError,
    MissingDependencyError,
    ValidationError,
    ValidationErrorDict
)
from .util import (
    get_in,
    is_json_object,
    is_json_array,
    is_json_string,
    is_json_number,
    is_json_bool,
)

try:
    from collections import OrderedDict as sorteddict
except ImportError:
    try:
        from ordereddict import OrderedDict as sorteddict
    except ImportError:
        sorteddict = dict
