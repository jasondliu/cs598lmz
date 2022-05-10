import ctypes
ctypes.cast(id(0), ctypes.py_object).value


# In[3]:

from tensorflow.core.framework import variable_pb2
import google.protobuf.text_format
import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import embedding_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import variable_scope

# def my_rnn(cell, inputs, initial_state=None, dtype=None,sequence_length=None, scope=None):
#     with variable_scope.variable_scope(scope or "rnn"):
#         # Create a new scope in which the caching device is either
#         # determined by the parent scope, or is set to place the cached
#         # Variable using the same placement as for the rest of the RNN.
#         with vs.variable_scope(variable_scope.get_variable_scope()) as v
