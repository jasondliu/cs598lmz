import types
types.ModuleType.__eq__ = lambda self, other: self is other

from argparse import ArgumentParser
from collections import OrderedDict
from datetime import datetime
from functools import partial
from itertools import product
import os
from pathlib import Path
from pprint import pprint
from types import SimpleNamespace
import sys
from time import sleep
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from tqdm import tqdm

from d3m import container, exceptions, index, metadata, utils as d3m_utils
from d3m.base import utils as d3m_base_utils
from d3m.container import DataFrame as d3m_DataFrame
from d3m.metadata import base as metadata_base, hyperparams as hyperparams_module, params as params_module
from d3m.metadata.base import ArgumentType, Context, Metadata
from d3m.metadata.hyperparams import Hyperparams
from d3m.metadata.params import Params
from d3m
