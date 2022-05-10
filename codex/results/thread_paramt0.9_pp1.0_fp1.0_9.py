import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler

# load in data and create data loaders
import numpy as np
import torch.utils.data

def get_data_loader(batch_size):
    import torchvision.datasets as datasets
    import torchvision.transforms as Transforms
    
    normalize = Transforms.Normalize(mean=[0.5, 0.5, 0.5],
                                     std=[0.5, 0.5, 0.5])
    
    transform = Transforms.Compose([Transforms.ToTensor(), normalize])
    
    train_set = datasets.CIFAR10(root='./data', train=True,
                                    download = True, transform = transform)
    
    test_set = datasets.CIFAR10(root='./data', train=False,
                                   download = True, transform = transform)
    
    train_loader = torch
