import mmap
import socket
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from aiohttp import ClientError
from hyperas import optim
from hyperopt import Trials, STATUS_OK, fmin, tpe
from hyperopt.pyll import scope
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from dffml.base import config, field, Input, output
from dffml.df.base import op
from dffml.df.types import Definition
from dffml.model.accuracy import Accuracy
from dffml.model.args import ModelArg, estimator
from dffml.model.model import ModelContext
from dffml.model.predict import Predict
from dffml.model.trainer import BaseTrainer
from dffml.source.ops import (
    read_file_from_http,
    read_http,
    read_raw_http,
    read_file_from_http,
)
from dffml.source.source import Sources
from d
