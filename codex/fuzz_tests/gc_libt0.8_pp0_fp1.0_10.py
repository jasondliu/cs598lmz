import gc, weakref
import copy
from weakref import WeakSet
from pprint import pformat

from .jsonable import Jsonable
from . import utils


NO_DOCSTRING = "No docstring"


def _repr_html(value):
    """ A function to short-circuit docstring rendering, to prevent the
    recursive calls which automatically trigger on any and all objects.
    """
    return "HTML(%r)" % pformat(value)


class HasProps(Jsonable):
    """
    Base class for all plot-related objects. ``HasProps`` implements
    functionality to make it easy to declare properties on a class,
    including:

    * All of these attributes are documented using the class docstring,
      which is searched for a section with a heading that matches
      the property name (see next section for details)

    * Default values may be specified by an expression in a string.
      These expressions are evaluated at class definition time,
      allowing the default values to depend on other properties of the
      class.

    * Properties may be declared 'read only' to prevent them from being
     
