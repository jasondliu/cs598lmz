import gc, weakref
import numpy as np
import pytest

import numba as nb
import numba.core.errors
from numba.core import config, types, utils
from numba.core.compiler import compile_isolated, Flags
from numba.core.compiler_lock import global_compiler_lock
from numba.core.ir_utils import (
    guard,
    guard_recursion,
    lift_to_top,
    lower_builtin,
    lower_getattr,
    lower_getitem,
    lower_setattr,
    lower_setitem,
    remove_dels,
    remove_dead,
    remove_mutable_args,
    remove_unreachable,
    replace_arg_nodes,
    replace_call_nodes,
    replace_const_nodes,
    replace_invalid_ops,
    replace_invalid_ops_with_call,
    replace_mutable_vars,
    replace_vars_with_const,
    run_dce,
    run_dce_on_
