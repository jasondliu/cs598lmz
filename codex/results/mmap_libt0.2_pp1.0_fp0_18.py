import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool
from operator import itemgetter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
import pysam
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC
from tqdm import tqdm

from . import __version__
from .constants import (
    ANNOTATION_COLUMNS,
    ANNOTATION_COLUMNS_WITH_SEQ,
    ANNOTATION_COLUMNS_WITH_SEQ_AND_QUAL,
    ANNOTATION_COLUMNS_WITH_SEQ_AND_QUAL_AND_CIGAR,

