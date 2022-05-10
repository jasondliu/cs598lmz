import mmap
import numpy as np
import os
import pandas as pd
import re
import requests
import shutil
import sys
import tarfile
import tempfile
import time
import zipfile

from collections import defaultdict
from datetime import datetime
from functools import partial
from io import BytesIO
from multiprocessing import Pool
from pathlib import Path
from urllib.parse import urlsplit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn
import torch.utils.data
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch.optim import lr_scheduler
from torch.optim.lr_scheduler import StepLR, ReduceLROnPl
