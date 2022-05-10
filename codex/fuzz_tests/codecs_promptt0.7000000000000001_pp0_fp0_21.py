import codecs
# Test codecs.register_error('replace_with_space', ...
import random
import os, re
from tqdm import tqdm
def read_lines(filename):
    """Read all the lines in a text file and return as a list
    """
    with codecs.open(filename, 'r', 'utf-8') as f:
        return [line.strip() for line in f]
def build_dataset(filename):
    """Read query, response pairs and return a dictionary that maps each query
    to a list of responses, and a list of all queries and responses
    """
    lines = read_lines(filename)
    id2line = {}
    for line in lines:
        _line = line.split(' +++$+++ ')
        if len(_line) == 5:
            if _line[0] not in id2line:
                id2line[_line[0]] = []
            id2line[_line[0]].append({'utterance_id':_line[1],
                                      'movie_id':_line[2],
                                      'character_id':_line[3],
