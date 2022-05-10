import select_study_set
import numpy as np
import time
import math
import sys

def get_result(options, rank_list, gtItem):
    precision = np.zeros((5))
    recall = np.zeros((5))
    for i in range(5):
        precision[i] = 0.0
        recall[i] = 0.0

    hit = 0
    for i in range(len(rank_list)):
        item = rank_list[i]
        if item == gtItem:
            hit = 1
            break
    precision[0] = hit
    recall[0] = hit
    for i in range(1, 5):
        if len(rank_list) >= i + 1:
            item = rank_list[i]
            if item == gtItem:
                hit = hit + 1
            precision[i] = hit * 1.0 / (i + 1)
            recall[i] = hit * 1.0 / (1)
    return precision, recall
