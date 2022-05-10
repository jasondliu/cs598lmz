import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
wc = 0

def foo():
    global wc
    wc += 1
    print(f'called {wc} times')    
    
signal.siginterrupt(signal.SIGALRM, False)
signal.signal(signal.SIGALRM, lambda x,y: foo())

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.pause()

 

## Tensorboard

import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt

# Hyper Parameters
input_size = 784
hidden_size = 500
num_classes = 10
num_epochs = 5
batch_size = 100
learning_rate = 0.001

# MNIST Dataset (Images and Labels)
train_dataset = d
