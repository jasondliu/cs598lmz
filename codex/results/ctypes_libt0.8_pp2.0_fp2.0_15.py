import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')

import caffe2.python.onnx.backend as backend

model = "simple_graph.onnx"

outputs = backend.prepare(model).run(np.random.random(size=(1, 3, 224, 224)).astype(np.float32))

print (outputs)
