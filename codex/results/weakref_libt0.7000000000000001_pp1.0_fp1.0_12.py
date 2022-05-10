import weakref
from sklearn.manifold import TSNE

from cv2 import cv2
from tqdm import tqdm

from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
from torchvision.models import resnet18
from torch import nn

from .transforms import RandomCrop, CenterCrop, RandomHorizontalFlip
from .transforms import Augmentation, Resize, ToTensor, Normalize, Transform

from .loader import *
from .dataset import *

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from network import *
from data_loader import *
from dataset import *
from evaluation import *
from feature import *

class ResNet_Embedding(nn.Module):
    def __init__(self, embedding_size, num_classes, pretrained=False, gpu=True):
        super(ResNet_Embedding, self).__init__()
        
        if pretrained:
            resnet = resnet18(pretrained=True
