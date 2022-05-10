import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')
import caffe2.python.onnx.backend as backend
import numpy as np
import onnx

model = onnx.load('mnist.proto')
rep = backend.prepare(model, device='CUDA')

print('The model is prepared!')

# run the model in Caffe2

outputs = rep.run(np.random.randn(1, 1, 28, 28).astype(np.float32))

print('Running the model in Caffe2!')

print(outputs[0])
