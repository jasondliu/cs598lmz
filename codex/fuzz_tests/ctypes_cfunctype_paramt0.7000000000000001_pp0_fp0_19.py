import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

import numpy as np

from lib.sigmoid import sigmoid
from lib.sigmoid import sigmoid_derivative
from lib.sigmoid import sigmoid_x

import lib.utils as utils

class NeuralNetwork:
    def __init__(self, layer_sizes, input, output):
        if len(layer_sizes) < 3:
            raise ValueError('Layer sizes must be of length 3 (at least)')

        self.layer_sizes = layer_sizes
        self.num_layers = len(layer_sizes)
        self.input = input
        self.output = output
        self.weights = []
        self.biases = []
        self.expected_output = None
        self.learning_rate = None
        self.cost_function = None
        self.cost_derivative = None

        # initialize biases and weights
        for i in range(self.num_layers):
            if i == 0:
                continue

            if
