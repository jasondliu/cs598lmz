import ctypes
ctypes.cdll.LoadLibrary('/usr/local/cuda/lib64/libcudart.so')

import onnxruntime
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image

session = onnxruntime.InferenceSession('/usr/share/onnxruntime/models/faster_rcnn/model.onnx')

imgs = [Image.open('images/'+f) for f in os.listdir('images/')]
img = imgs[0]
img = img.resize((300, 300))

img_ycbcr = img.convert('YCbCr')
img_y, img_cb, img_cr = img_ycbcr.split()

x = np.array(img_y)[np.newaxis, np.newaxis, :, :].astype(np.float32) - 128.

input_name = session.get_inputs()[0].name
label_name = session.get_outputs()[0].name
rois_name = session
