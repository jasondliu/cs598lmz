import mmap
import argparse
from math import *


def get_data(file):
    with open(file, 'r') as f:
        x = f.read()
    parsed = json.loads(x)
    return parsed


def get_tree(list):
    """
    Parse the tree into a dictionary
    :param list: List of dictionaries that contains the tree
    :return: Return a dictionary with eveything
    """
    out = {}
    for x in list:
        if 'children' in x.keys():
            out[x['title']] = get_tree(x['children'])
        else:
            out[x['title']] = {}
    return out


def create_full_tree(d, path=''):
    print(path)
    for x in d.keys():
        if path is not '':
            newpath = path + ' > ' + x
        else:
            newpath = x
        create_full_tree(d[x], newpath)
    return


def get_words_size(size, list):
