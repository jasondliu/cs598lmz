import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import argparse
import os
import random
import sys
import time

import numpy as np
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models

import torch.distributed as dist

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.multiprocessing import Process

import torch.distributed as dist

from torch.multiprocessing import Process

import torchvision
import torchvision.transforms as transforms

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import torch.distributed as dist
