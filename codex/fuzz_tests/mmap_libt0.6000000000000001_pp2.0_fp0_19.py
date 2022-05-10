import mmap
import os
import pickle
import random
import re
import shutil
import sys
import time
from collections import Counter
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime
from glob import glob
from itertools import chain
from math import ceil
from multiprocessing import Pool
from multiprocessing.util import Finalize
from subprocess import PIPE
from tempfile import NamedTemporaryFile

import boto3
import botocore
import click
import numpy as np
import pandas as pd
import pysam
import pytz
import rpy2
import rpy2.robjects as robjects
from biom import load_table
from biom.cli.table_summarizer import summarizer
from biom.util import biom_open
from rpy2.robjects import pandas2ri

from q2_types.feature_table import FeatureTable, BIOMV210Format
from q2_types.per_sample_sequences import (Sequences,
                                           CasavaOneEightSingleLanePerSampleDirFmt,
