import mmap
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import cohen_kappa_score, make_scorer, accuracy_score
from sklearn.metrics import confusion_matrix as sk_cmatrix
from skimage.morphology import binary_opening, disk
from skimage.io import imread
from scipy.ndimage.morphology import binary_fill_holes
from skimage.morphology import label
from sklearn.metrics import jaccard_score

# PyTorch
import torch
from torch import nn
from torch.nn import functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader,Dataset
import torch.backends.cudnn as cudnn
from torch.optim.lr_scheduler import CosineAnnealingLR, MultiStepLR
from tqdm import tqdm
from pycm import ConfusionMatrix
from sklearn.metrics import confusion_matrix

from aug import *
import cv
