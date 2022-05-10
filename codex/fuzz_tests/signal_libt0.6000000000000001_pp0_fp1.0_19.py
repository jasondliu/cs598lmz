import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
import sys
sys.path.insert(0, "../../")
from ontology import ontology
import random
from ontology import assoc_management, loader, graph_mapping
from ontology.utils import open_file
from ontology.lib.graph import Graph
import pandas as pd
from ontology.lib.graph_tool_wrapper import GraphWrapper
import numpy as np
import argparse
from ontology.lib.util import get_ontology
from ontology.lib.bio.go import GODag
from ontology.lib.bio.io.gaf import GafReader
import networkx as nx
import os
from multiprocessing import Pool
from functools import partial
from ontology.utils.logger import get_logger
from ontology.lib.graph_tool_wrapper import GraphWrapper
from collections import Counter
LOGGER = get_logger("ontology_enrichment")

def get_module(ontology, module_file):
    module_
