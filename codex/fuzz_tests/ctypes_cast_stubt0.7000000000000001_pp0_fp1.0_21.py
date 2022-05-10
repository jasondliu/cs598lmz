import ctypes
ctypes.cast(None, ctypes.py_object)

#%%
import os
import tensorflow as tf

# Load the model exported by the object detection module.
# model_path = './inference_graph/frozen_inference_graph.pb'
model_path = '/home/adam/Desktop/models/research/object_detection/inference_graph/frozen_inference_graph.pb'
# model_path = '/home/adam/Desktop/models/research/object_detection/inference_graph/saved_model/saved_model/saved_model.pb'

# List of the strings that is used to add correct label for each box.
labels_path = os.path.join('/home/adam/Desktop/models/research/object_detection/training/labelmap.pbtxt')

# Load frozen tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(model_path
