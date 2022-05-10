from types import FunctionType
list(FunctionType(add.__code__, globals(), 'add'))

#%% test
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1 - np.tanh(x)**2

def relu(x):
    return np.maximum(x, 0)

def relu_prime(x):
    return (x>0) * 1.0

def step(x):
    return (x>0) * 1.0

def step_prime(x):
    return 0

import random
class NeuralNetwork:
    def __init__(self, layers, activation='sigmoid'):
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_prime
        elif
