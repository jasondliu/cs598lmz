import mmap
import re
import sys
import time

from google.protobuf import text_format

import caffe
from caffe.proto import caffe_pb2

# If your GPU is memory constrained, set this to a fraction of the default
# value of 0.95.
#
# If you have a very small net, you may be able to set this to a higher value,
# but be careful to monitor your GPU memory usage.
GPU_MEMORY_FRACTION = 0.95


def get_net(caffemodel, deploy_file, use_gpu=True):
    """
    Returns an instance of caffe.Net

    Arguments:
    caffemodel -- path to a .caffemodel file
    deploy_file -- path to a .prototxt file

    Keyword arguments:
    use_gpu -- if True, use the GPU for inference
    """
    if use_gpu:
        caffe.set_mode_gpu()

    # load a new model
    return caffe.Net(deploy_file, caffemodel, caffe.TEST)



