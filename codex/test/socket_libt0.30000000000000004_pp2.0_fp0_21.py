import socket
import threading
import time
import sys
import os
import signal
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.contrib.tensorrt as trt
from tensorflow.python.platform import gfile
from tensorflow.python.framework import graph_util

# 定义全局变量
# 定义模型路径
model_path = './model/'
# 定义模型名称
model_name = 'frozen_inference_graph.pb'
# 定义模型输入节点名称
input_node_name = 'image_tensor:0'
# 定义模型输出节点名称
