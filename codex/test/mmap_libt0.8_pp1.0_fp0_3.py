import mmap
import numpy as np
import torch
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
from torchvision import transforms
import tqdm

class TransformPair(Dataset):
    def __init__(self, data, labels=None, transforms=None):
        self.data = data
        self.labels = labels
        self.transforms = transforms
        
    def __len__(self):
        return len(self.data)

