import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

from collections import defaultdict
from contextlib import contextmanager
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

import attr
import click
import numpy as np
import pandas as pd
import scipy.stats
import seaborn as sns
import tqdm
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.col
