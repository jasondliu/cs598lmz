import gc, weakref
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.plasma as plasma
import time

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

from matplotlib import pyplot as plt

def get_data(file_name):
    # read parquet
    parquet_file = pq.ParquetFile(file_name)
    # read all columns
    columns = parquet_file.metadata.schema.names
    # read all data
    df = parquet_file.read(columns=columns).to_pandas()
    return
