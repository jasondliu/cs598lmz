import mmap
import os
import random
import string
import sys
import time

from numpy import *

sys.path.append(os.path.abspath("../lib"))
from util import *
import svm



def main():
    ### load data set from file
    print "loading data..."
    dataSet = []
    labels = []
    fileIn = open('testSet.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
        labels.append(float(lineArr[2]))
    dataSet = mat(dataSet)
    labels = mat(labels).transpose()
    train_x = dataSet[0:81, :]
    train_y = labels[0:81, :]
    test_x = dataSet[80:101, :]
    test_y = labels[80:101, :]

    print train_x.shape, train_y.shape, test
