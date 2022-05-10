import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')
sys.path.insert(0, os.getcwd())

from caffe2.python import core, workspace
from caffe2.proto import caffe2_pb2
from caffe2.python import dyndep

dyndep.InitOpsLibrary("//caffe2/caffe2/distributed:file_store_handler_ops")

from caffe2.python import rnn_cell
from caffe2.python import model_helper, brew, optimizer
from caffe2.python.modeling import initializers

from caffe2.python import rnn_cell
from caffe2.python import model_helper, brew, optimizer
from caffe2.python.modeling import initializers
from caffe2.python import rnn_cell, core, workspace, brew
from caffe2.python.modeling.parameter_info import ParameterTags

from caffe2.python import utils
import numpy as np

import logging
from caffe2.python import debugger


from caffe2.python import dyndep
from caffe2.python
