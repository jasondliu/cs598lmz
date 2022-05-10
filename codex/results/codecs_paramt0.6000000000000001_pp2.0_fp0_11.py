import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import os
import sys
import os.path
import re
import string
import argparse
import numpy as np

# add data_utils.py to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_utils import *

def process_data(data_path, data_file, new_data_file, word_dict_file,
                 label_dict_file, word_num_dict_file, label_num_dict_file,
                 word_cut_dict_file, label_cut_dict_file, word_cut_num_dict_file,
                 label_cut_num_dict_file, word_dict_size, label_dict_size,
                 min_word_frequency, min_label_frequency,
                 word_num_dict_size, label_num_dict_size,
                 min_word_num_frequency, min_label_num_frequency,
                 word_cut_dict_size, label_
