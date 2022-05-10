from bz2 import BZ2Decompressor
BZ2Decompressor
import pickle
import random
import sys, os, re
import tensorflow as tf
import numpy as np
import math

from sklearn.feature_extraction.text import TfidfVectorizer


def create_negs(pos_list, num, max_list_len):
    negative_list = []
    for x in range(len(pos_list)):
        negative_list.append([])
        for y in range(num):
            negative_list[x].append(random.randint(0,max_list_len-1))

    return np.array(negative_list)

def gen_pairs(graphs_list, title_list, negative_list, num_neg):
    title_value = 1.0 / (num_neg + 1)
    neg_value = -1.0 / (num_neg + 1)
    data = []
    for i in range(len(graphs_list)):
#        print("Positive whole list", graphs_list[i][negative_list[i][0]])
#        print("Positive
