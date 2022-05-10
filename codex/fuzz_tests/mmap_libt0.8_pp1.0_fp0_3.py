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

    def __getitem__(self, idx):
        img = self.data[idx]
        if self.labels is not None:
            label = self.labels[idx]
        if self.transforms is not None:
            img = self.transforms(img)
        if self.labels is not None:
            return img, label
        else:
            return img

class TransformPairCNN(Dataset):
    def __init__(self, data, labels, input_transform=None, output_transform=None):
        self.data =
