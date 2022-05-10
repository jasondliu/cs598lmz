import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')
from caffe2.python import core, workspace
from caffe2.proto import caffe2_pb2
import numpy as np
from caffe2.python import rnn_cell
from caffe2.python.modeling import initializers
from caffe2.python.model_helper import ModelHelper


init_net = caffe2_pb2.NetDef()
with open('./init_net.pb', 'rb') as input_init_net:
    init_net.ParseFromString(input_init_net.read())
init_net.device_option.CopyFrom(core.DeviceOption(caffe2_pb2.CUDA, 0))

# Initialize the RNNModelHelper
model = ModelHelper(name="lstm_model", init_params=True)

# Pass in the init net def to the RNN model in order to initialize RNN states
model.param_init_net = init_net

# This creates the input blobs used to feed sequence data as input to the model
seq_lengths =
