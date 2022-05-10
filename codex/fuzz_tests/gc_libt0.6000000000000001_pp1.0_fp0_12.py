import gc, weakref, collections

from . import util
from . import exceptions
from . import internals
from . import type_registry

from .internals import *
from .util import *
from .exceptions import *
from .type_registry import *


# TODO:
# - Add a 'one_of' type, which works like a SubDict, but is not a dictionary
#   and doesn't allow setting other keys.
# - Add a 'validator' type, which validates the value every time it's set,
#   and returns an error message if it's wrong.

# TODO:
# - Use the 'doc' attribute instead of the 'help' parameter.
# - Make it possible to set the type in the __init__ method.
# - Add a 'default' parameter, which is used if the value is not set.
# - Add a 'name' parameter, which is used to look up the value in the
#   configuration.
# - Add a 'section' parameter, which is used to group the values.
# - Add a 'sub_section' parameter, which is used to group the
