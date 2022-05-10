import mmap
import sys
import time

import numpy as np

from utils import (
    get_database_connection,
    get_dataset,
    get_dataset_path,
    get_reconstruction_model,
    get_segmentation_model,
)

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

batch_size = 50

# Load dataset
if sys.platform.startswith("win"):
    root = "D:/Datasets"
else:
    root = "/home/john/Datasets"
