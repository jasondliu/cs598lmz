import types
types.SimpleNamespace = types.ModuleType("SimpleNamespace")

import sys
import os
import re
import argparse
import logging
import time

import numpy as np
import tensorflow as tf

from utils import get_model_fn
from utils import get_loss_fn
from utils import get_metric_fn
from utils import get_optimizer
from utils import get_input_fn
from utils import get_prediction_fn

# tf.enable_eager_execution()

# TF_CONFIG = json.loads(os.environ['TF_CONFIG'])
# TF_CONFIG = {
#     "cluster": {
#         "worker": ["localhost:12345", "localhost:23456", "localhost:34567"],
#         "ps": ["localhost:23456", "localhost:34567"]
#     },
#     "task": {
#         "type": "worker",
#         "index": 0
#     }
# }

def get_model_dir(args):
    model_dir = args
