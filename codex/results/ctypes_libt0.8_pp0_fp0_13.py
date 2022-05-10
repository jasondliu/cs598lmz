import ctypes
ctypes.WinDLL(os.path.join(winpython_dir, 'python-3.4.3.amd64', 'python34.dll'))

import numpy as np
np.random.seed(42)

import torch
torch.set_num_threads(1)
torch.manual_seed(42)
import torch.nn as nn

import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

import theano
theano.config.floatX = 'float32'
theano.config.device = 'cpu'
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv

from pylearn2.datasets.mnist import MNIST
mnist_train = MNIST(which_set = 'train')
mnist_test = MNIST(which_set = 'test')
X_train = mnist_train.get_topological_view().astype('float32') / 255
X_test =
