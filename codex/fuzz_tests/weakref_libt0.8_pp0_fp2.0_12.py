import weakref

from rpython.annotator.model import SomeInstance
from rpython.annotator.policy import AnnotatorPolicy
from rpython.translator.backendopt.canraise import RaisesException
from rpython.translator.backendopt.call import CallOptimizer, call_may_force
from rpython.translator.backendopt.inline import auto_inlining_of_small_functions
from rpython.translator.backendopt.removeops import remove_same_as
from rpython.translator.backendopt.ssa import DataFlowFamilyBuilder
from rpython.translator.backendopt.ssa import SSA_STATE_UNINITIALIZED
from rpython.translator.backendopt.ssa import SSA_STATE_INITIALIZED
from rpython.translator.backendopt.ssa import SSA_STATE_MAY_INITIALIZED
from rpython.translator.backendopt.ssa import remove_empty_blocks
from rpython.translator.backendopt.ssa import remove_asserts
from rpython
