import ctypes
# Test ctypes.CField instance to test ctypes.CField.show
from _testcapi import POINTER, _testfunc, _testfunc_p_if
from _ctypes.basics import _CData, CField, CData, CFuncPtr
from _ctypes.basics import _Pointer
from _ctypes.basics import sizeof, byref
from _ctypes.basics import _CDataMeta
from _ctypes.basics import _self_as_parameter_
from _ctypes import Union
from _ctypes import _SimpleCData
from ctypes import Structure
from hypothesis import given
from hypothesis._strategies import _is_buffer
from hypothesis.strategies import sampled_from
from hypothesis._settings import Settings
from hypothesis.stateful import RuleBasedStateMachine
from hypothesis.stateful import run_state_machine_as_test
from setup_tests import *


set_settings(deadline=None)


#
# This testcase *should not* be run with -O (python -OO -m test test_ctypes)
#
# It tests the ctypes module itself, and so it's
