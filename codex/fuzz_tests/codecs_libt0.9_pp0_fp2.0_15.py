import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys
sys.path.append('../')
import re
import os
import argparse
import json
import pickle
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# plot filter
# plot filter width
# plot discretized filter
# plot filter derivation
# plot filter derivation for discretized
# plot filter for 1 selected filter, for all filters
# plot filter for 1 dataset, for all datasets
# plot filter effects (dilation) with same filter width = 3, 1 selected filter
# plot filter effects (dilation) with all filters width = 3
# plot filter effects (dilation) with width = all filters
# plot filter effects (dilation) with all filters and widths
# plot filter table, visualizing all filter patterns

# plot time


def parse_sentence(sentence, rel_idx):
    root = 0
    parse = {}
    for i, rel in enumerate(reversed(sentence
