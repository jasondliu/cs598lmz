import threading
threading.stack_size(2048*2048)

import sys
sys.path.append("../")

import src.cifar10_util as cifar10_util

from tensorflow.python import pywrap_tensorflow
reader = pywrap_tensorflow.NewCheckpointReader('./model/ResNet_FuseBN/model.ckpt')
var_to_shape_map = reader.get_variable_to_shape_map()

for key in var_to_shape_map:
    print("tensor_name: ", key)
print(reader.get_tensor('absfuse/b1'))



NUM_CLASSES = cifar10_input.NUM_CLASSES


def resnet_layer(inputs,
                 num_filters=16,
                 kernel_size=3,
                 strides=1,
                 activation='relu',
                 batch_normalization=True,
                 conv_first=True,
                 name=None):
    conv = Conv2D(num_filters,
                  kernel_size=kernel
