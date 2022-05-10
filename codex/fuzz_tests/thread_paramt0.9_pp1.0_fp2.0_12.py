import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os

import torch.utils.data
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms

from .dataset import MSCelebDataset, MSCelebAttributeDataset


def get_dataloader(cfg, root_path):
  transform = transforms.Compose([
      transforms.Resize((cfg.im_size, cfg.im_size)),
      transforms.ToTensor(),
      transforms.Normalize(mean=(0.5,0.5,0.5), std=(0.5,0.5,0.5))
    ])

  if 'attribute' in cfg.dataset:
    root_path = os.path.join(root_path, 'MSCelebAttri')

    use_loader = cfg.loader_type == 'dataloader'

    if cfg.dataset == 'attribute':
      dataset = MSCelebAttributeDataset(os.path.
