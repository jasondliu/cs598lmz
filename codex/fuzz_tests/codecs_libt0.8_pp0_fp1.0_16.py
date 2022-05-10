import codecs
codecs.register(codecs.lookup("mbcs")) #fixing a bug on ssh server
import numpy as np
import scipy as sp
import scipy.io as sio
import matplotlib.pyplot as plt
import copy
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, NuSVC
from sklearn import preprocessing
import sys

from xlrd import open_workbook
from xlutils.copy import copy

#sys.path.append("D:/Users/chenzheng/Dropbox/Python/")
sys.path.append("D:/Users/chenzheng/Dropbox/Python/")


import pySpectralAnalysis as psa

def loadXLSfile(fileName, sheetID):
    wb = open_workbook(filename = fileName)
    sheetNum = wb.nsheets
    if sheetID > sheetNum:
        print "Invalid sheetID"
        return
    sheet = wb.sheet_by_
