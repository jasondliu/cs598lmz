import gc, weakref
from rpython.jit.metainterp.history import TreeLoop, BoxInt, ConstInt,\
     ConstPtr, AbstractDescr, BasicFailDescr, Box, BoxPtr
from rpython.jit.metainterp.resoperation import rop, ResOperation, OpHelpers
from rpython.jit.metainterp.typesystem import llhelper, OOtypeHelpers
from rpython.jit.metainterp.optimizeopt.optimizer import optimize_trace,\
     Optimization, OptimizationInfo
from rpython.jit.metainterp.optimizeopt.intutils import IntBound, IntUnbounded
from rpython.jit.metainterp.optimizeopt.util import args_dict, make_dispatcher_method
from rpython.jit.metainterp.optimizeopt.info import AbstractValue
from rpython.jit.metainterp.optimizeopt.vars import (VariableTracker,
                                                     VariableTrackerWithSimpleEquality,
                                                     VarIndex,
                                                     VarInfo,
                                                     LABEL)
from
