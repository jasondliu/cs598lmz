import ctypes
ctypes.CDLL("libatlas.so", mode=ctypes.RTLD_GLOBAL)
ctypes.CDLL("liblapack.so", mode=ctypes.RTLD_GLOBAL)
from scipy.stats import multivariate_normal
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import StandardScaler
import torch.nn as nn
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import accuracy_score
from torch import optim
import numpy as np
import time
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import csv

np.random.seed(12345
