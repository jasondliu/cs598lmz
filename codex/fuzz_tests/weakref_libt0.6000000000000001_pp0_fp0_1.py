import weakref

import numpy as np

from . import errors
from . import types
from . import utils
from . import version
from .cpp import (CPP_MODE, CPP_MODES, CPP_INT_TYPES, CPP_FLOAT_TYPES,
                  CPP_COMPLEX_TYPES, CPP_BOOL_TYPES, CPP_STRING_TYPES,
                  CPP_STD_STRING_TYPES, CPP_INT_SUBTYPES, CPP_FLOAT_SUBTYPES,
                  CPP_COMPLEX_SUBTYPES, CPP_BOOL_SUBTYPES, CPP_STRING_SUBTYPES,
                  CPP_STD_STRING_SUBTYPES, cpp_typeinfo, cpp_typecode,
                  cpp_type_from_typecode, cpp_type_from_varname,
                  cpp_type_from_arg, cpp_string_type, cpp_std_string_type,
                  c
