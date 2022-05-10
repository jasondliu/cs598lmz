import ctypes
ctypes.cast(0, ctypes.py_object).value

# -*- coding: utf-8 -*-
import numpy as np
import math
from matplotlib import pyplot as plt
from numpy import *
import os

#读取数据
def loadDataSet(filename):
    #记录特征数目
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

#求回归系数w
def standRegres(xArr, yArr
