import ctypes
ctypes.cast(0, ctypes.py_object)

import sys

# This is a bit (!) hacked together, in that it's hard-coded to only work for the
# specified input dimensions.
class ConvNet(object):
    def __init__(self, input_dim=(1, 28, 28), 
                 conv_spec=[
                     {'filter_size': 5, 'pad': 0, 'stride': 1, 'num_filters': 20},
                     {'filter_size': 5, 'pad': 0, 'stride': 1, 'num_filters': 50},
                     {'filter_size': 4, 'pad': 0, 'stride': 1, 'num_filters': 500},
                     {'filter_size': 1, 'pad': 0, 'stride': 1, 'num_filters': 10}],
                 hidden_dim=500, weight_scale=1e-3, reg=0.0,
                 dtype=np.float32):
        """
        Initialize a new network.
        
        Inputs:
        - input_dim: Tuple (C
