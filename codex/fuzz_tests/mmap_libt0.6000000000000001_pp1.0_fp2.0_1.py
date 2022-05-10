import mmap
import numpy as np
import os
import struct
import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as data
import torchvision
import torchvision.transforms as transforms

from pdb import set_trace as bp

class VOCDetection(data.Dataset):
    def __init__(self, root, image_set, transform=None, target_transform=None):
        self.root = root
        self.image_set = image_set
        self.transform = transform
        self.target_transform = target_transform
        self.name = 'voc'
        self.ids = list()
        for line in open(os.path.join(root, 'ImageSets', 'Main', image_set + '.txt')):
            self.ids.append((self.root, line.strip()))

    def __getitem__(self, index):
        im, gt, h, w = self.pull_item(index)

        return im, gt

    def __len__(
