import mmap
import networkx as nx
import numpy as np
import os
import pickle
import random
import shutil
import sys
import textwrap
import threading
import time
from collections import defaultdict, namedtuple

from common import get_hpo_terms

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import NamespaceManager

from simstring.database.dict import DictDatabase
from simstring.measure.cosine import CosineMeasure

import pyobo

from simstring.database.dict import DictDatabase
from simstring.measure.cosine import CosineMeasure

from pyobo.sources.hpo import get_hpo_obo

import coloredlogs, logging
coloredlogs.install(level=logging.DEBUG)

sys.path.append('/home/michael/jensenlab/motif_inference/src')
from utils import dsd

GO_EDGE_COUNT = 1859853

CANDIDATE_COUNT = 100

def get_
