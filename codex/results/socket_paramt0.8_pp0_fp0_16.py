import socket
socket.if_indextoname('167772184')

import tkinter 
from tkinter import filedialog
import os
os.getcwd()
root = tkinter.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

import numpy as np
import pandas as pd
data = pd.read_csv(file_path, sep=',',header=None)
data = np.array(data)
#data = np.array(data, dtype=None, order=None, copy=True, subok=False, ndmin=0)

#data[:,0] = data[:,0]/10**9

import datetime
data[:,0] = data[:,0]/10**9
data[:,0] = data[:,0] - data[0,0] #start at 0
data[:,0] = data[:,0].astype(int)
data[:,0] = data[:,0].astype(str)
for i in range(data.shape[0]):
    seconds = data[i
