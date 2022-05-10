import types
types.ModuleType.__call__ = lambda self, *args, **kwargs: self
import sys
sys.modules['__main__'] = types.ModuleType('__main__')
sys.modules['__main__'].__dict__.update(globals())
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import torch
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader
import torch.nn.functional as F
from torch.autograd import grad
from torch.nn.modules.loss import MSELoss
from torch.nn.modules.loss import _Loss
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.optim.lr_scheduler import MultiStepLR
from torch.optim.lr_scheduler import StepLR
from torch.optim.
