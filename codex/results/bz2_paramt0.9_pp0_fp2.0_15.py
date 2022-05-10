from bz2 import BZ2Decompressor
BZ2Decompressor()
sys.path.insert(0, '/home/mengjiao/Desktop/Tomviz/tomviz/src/RemotePython')
import numpy as np 
from future import builtins
from io import BytesIO
import rpyc
import random
import time
import sys
import os
import subprocess
import pickle
import struct
try:
    from pyne.mesh import Mesh
    from pyne import material
except:
    print ("Pyne needs to be installed")
import h5py

# Define a list of IP address to access
ip_list = ['10.8.0.1']

# Split filename into name and extension
def get_filename(path):
    name, ext = os.path.splitext(os.path.basename(path))    
    return name

# Load data from file
def load_data(path, unit=0.1):
    f = open(path, "rb")
    data = pickle.loads(f.read())
    f.close()
    #unit = data['unit']
    #data =
