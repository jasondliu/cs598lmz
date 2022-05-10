import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')

# caffe2 lib
import sys
sys.path.append(path_to_caffe2_pybind11)
sys.path.append(path_to_caffe2_build)
import caffe2

# import caffe2.python.onnx.frontend
import onnx
from caffe2.python import core, workspace, models, optimizer, net_drawer, utils, visualize

import numpy as np
import skimage.io
import skimage.transform
import matplotlib.pyplot as plt
from PIL import Image
# set device option
device_opts = core.DeviceOption(caffe2.python.caffe2_pybind11.CUDA, 0)
onnx_model = onnx.load("mobilenetv2-1.0.onnx")
init_net, predict_net = caffe2.python.onnx.frontend.caffe2_net(onnx_model)

#init_net.Proto().device_option
