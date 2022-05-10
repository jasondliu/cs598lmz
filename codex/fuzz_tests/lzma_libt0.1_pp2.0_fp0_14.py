import lzma
lzma.LZMAError

import os
import sys
import time
import json
import shutil
import logging
import argparse
import subprocess
import multiprocessing
import threading
import concurrent.futures

import numpy as np
import pandas as pd

from tqdm import tqdm
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

from . import utils
from . import config
from . import constants
from . import __version__

logger = logging.getLogger(__name__)

def get_parser():
    parser = argparse.ArgumentParser(
        description='Runs the pipeline for the given dataset.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--version', action='version', version=__version__)

    parser.add_argument('--dataset', type=str, required=True,
                        help='The dataset to run the pipeline on.')

    parser.add_argument('--
