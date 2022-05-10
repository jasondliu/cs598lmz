import mmap
import numpy as np
import os
import pickle
import random
import sys
import time
from tqdm import tqdm
from multiprocessing import Pool

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler
from torchvision import transforms

from datasets import ImageDataset
from models import Generator
from utils import get_config, get_data_loader, init_model, init_random_seed, save_and_cleanup, save_image

def main(config):
    # For fast training
    if config.master_batch_size is None:
        config.master_batch_size = config.batch_size
    config.batch_size = config.master_batch_size // config.num_gpus
