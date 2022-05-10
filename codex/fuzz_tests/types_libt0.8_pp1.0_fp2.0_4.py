import types
types.ModuleType
import os
import re
import json
import ast
import pandas as pd
from . import constants as c
from . import data_tools
from . import semantic_tools
from . import reporting
from . import utilities

# import preprocessing.data_tools
# import preprocessing.semantic_tools
# import preprocessing.reporting
# import preprocessing.utilities

def load_dict(in_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        dic = json.load(f)
    return dic


def load_csv_table(in_file, delimiter=','):
    table = pd.read_csv(in_file, delimiter=delimiter, index_col=0, na_filter=False, keep_default_na=False)
    return table

def load_info(in_file, sheet_name=0):
    with open(in_file, 'r') as f:
        info = json.load(f)
    return info

# def load_data(dic
