import mmap
import numpy as np
import os
import sys
import time

sys.path.append("../../python")
import caffe

#import matplotlib.pyplot as plt
#%matplotlib inline

caffe_root = '/home/krishna/caffe/'  # this file is expected to be in {caffe_root}/examples
sys.path.insert(0, caffe_root + 'python')

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = caffe_root + 'models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = caffe_root + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
IMAGE_FILE = caffe_root + 'examples/images/cat.jpg'

net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load(caffe_
