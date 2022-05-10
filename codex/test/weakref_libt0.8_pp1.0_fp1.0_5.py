import weakref

from tensorflow.python.eager import context
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import gen_math_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import resource_variable_ops
from tensorflow.python.ops import state_ops
from tensorflow.python.ops import variables
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.training import optimizer
from tensorflow.python.training import training_ops


class SDCAOptimizer(optimizer.Optimizer):
  """Stochastic Dual Coordinate Ascent Optimizer for linear models with L1+L2
    regularization.

    As global optimization objective is strongly-convex, the optimizer optimizes
    the dual objective at each step. The optimization variables are the dual
    weights, which are computed from the primal weights and dual learning rate.
  """

