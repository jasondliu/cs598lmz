import ctypes
ctypes.cdll.LoadLibrary("caffe2_nvrtc.dll")
import caffe2.python.onnx.backend as onnx_caffe2_backend
import numpy as np
import onnx
import sys

# Load the ONNX model
model = onnx.load("model.onnx")

# check that the IR is well formed
onnx.checker.check_model(model)

# Print a human readable representation of the graph
onnx.helper.printable_graph(model.graph)
print("\n")

# prepare the caffe2 backend for executing the model this converts the ONNX model into a
# Caffe2 NetDef that can execute it. Other ONNX backends, like one for CNTK will be
# availiable soon.
prepared_backend = onnx_caffe2_backend.prepare(model)

# run the model in Caffe2
W = {model.graph.input[0].name: np.random.randn(1,3,224,224).astype(
