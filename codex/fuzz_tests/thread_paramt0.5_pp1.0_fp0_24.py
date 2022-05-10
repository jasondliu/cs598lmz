import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from IPython.display import clear_output

from tqdm import tqdm, trange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import torchvision
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torchvision.models import resnet18
from torchvision import models

from torch import nn
import torch
from torch.nn import functional as F
from torch import optim

import sklearn
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.metrics import confusion_matrix

from PIL import Image


