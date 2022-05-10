import types
types.ModuleType.__setattr__ = types.ModuleType.__setattr__

# a scikit-learn requires that numpy is imported before sklearn
import numpy as np

# project internal modules
from auto_yolo import cfg
from yolov3 import load_model, load_labels, plot_bboxes, save_img, post_process_boxes
from auto_yolo.label_generator import get_label_map, get_label_for_raw_detection
from auto_yolo.detection_embedding import get_detection_embedding_np, get_detection_embedding_mul, get_detection_embedding
from auto_yolo.clustering import get_k_means, METRIC_PRECOMPUTED, METRIC_EUCLIDEAN
from auto_yolo.internal.utils import get_bboxes_via_k_means


class AutoYolo:
    def __init__(self, config_file, weights_file=None, labels_file=None, image_size=None, gpu=False, labels_
