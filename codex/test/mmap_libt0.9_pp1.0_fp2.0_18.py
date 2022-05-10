import mmap
import numpy as np
import time
import json
import copy
import pprint
import math
import codecs
import sys
import os

from os import listdir
from os.path import isfile, join

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from PIL import Image
import torchvision.transforms.functional as TF
from torch.utils.data.sampler import Sampler

class MotsBatchSampler(Sampler):
	def __init__(self, data_source, batch_size=20, shuffle=True):
		self.data_source = data_source
		self.batch_size = batch_size
		self.shuffle = shuffle

	def __iter__(self):
		batch = []
		if self.shuffle:
			for idx in torch.randperm(len(self.data_source)):
				if len(batch) == self.batch_size:
					batch_copy = copy.deepcopy(batch)
		
