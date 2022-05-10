import types
types.ModuleType.__dict__.__setitem__('__getattr__', lambda self, name: __import__(name))

# import cv2
import numpy as np
import os
import sys
import time
import cv2
import argparse

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../common'))

from yolo_utils import construct_yolo_tensors
from yolo_utils import yolo_boxes_to_corners
from yolo_utils import yolo_filter_boxes
from yolo_utils import iou
from yolo_utils import yolo_non_max_suppression
from yolo_utils import draw_boxes
from yolo_utils import yolo_eval
from yolo_utils import yolo_head
from yolo_utils import yolo_output_to_boxes
from yolo_utils import preprocess_image
from yolo_utils import scale_boxes

from tensorflow.python.keras.layers import Input
from tensorflow
