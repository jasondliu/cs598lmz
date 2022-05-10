import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys

# SOURCE LINE 5

from pypy.rpython.lltypesystem import lltype, rffi
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.ootypesystem import ootype
from pypy.rpython.annlowlevel import llhelper
from pypy.rpython.annlowlevel import hlstr
from pypy.rpython.annlowlevel import llstr
from pypy.rpython.annlowlevel import cast_instance_to_base_ptr
from pypy.rpython.annlowlevel import cast_base_ptr_to_instance
from pypy.rpython.annlowlevel import cast_base_ptr_to_instance_maybe
from pypy.rpython.annlowlevel import cast_object_to_ptr
from pypy.rpython.annlowlevel import cast_ptr_to_object
from pypy.rpython.annlowlevel import cast_ptr_to_int
