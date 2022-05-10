import gc, weakref
import os
import sys
import types

from src.lib.constants import *
from src.lib.instructions_lib import *
from src.lib.instructions_lib import _int_instructions
from src.lib.instructions_lib import _ref_instructions
from src.lib.instructions_lib import _float_instructions
from src.lib.instructions_lib import _void_instructions
from src.lib.instructions_lib import _unary_instructions
from src.lib.instructions_lib import _binary_instructions
from src.lib.instructions_lib import _switch_instructions
from src.lib.instructions_lib import _array_instructions
from src.lib.instructions_lib import _ternary_instructions
from src.lib.instructions_lib import _type_instructions
from src.lib.instructions_lib import _field_instructions
from src.lib.instructions_lib import _method_instructions
from src.
