import lzma
lzma.LZMAError

from pprint import pprint

from typing import List, Dict, Union

from pathlib import Path
from itertools import chain

import json
import dataclasses

from typing import List, Dict, Tuple, Union
from collections import defaultdict

from bs4 import BeautifulSoup

from loguru import logger

from dataclasses import dataclass

from itertools import zip_longest

import numpy as np
import pandas as pd

from tqdm import tqdm

import re
import os

from pathlib import Path
from collections import Counter
from collections import defaultdict
from typing import List, Dict, Tuple, Union
from itertools import chain

from sklearn.model_selection import train_test_split

from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score, confusion_matrix

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticReg
