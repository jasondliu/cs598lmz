import mmap
import argparse
import os
import time
import sys
import numpy as np
from matplotlib import pyplot as plt

from hdf5_image_processing import Hdf5ImageProcessingLib as IPL
from hdf5_processing import RecursiveDict as rdict

def main():
    parser = argparse.ArgumentParser(description='Plot FFTs from HDF5-files')
    parser.add_argument('hdf5_file', action='store', type=str, help='HDF5-file')
    parser.add_argument('-d', '--dataset', action='store', type=str, default='/data/images/', help='HDF5-dataset')
    parser.add_argument('-m', '--metadata', action='store', type=str, default='/data/', help='HDF5-metadata')
    parser.add_argument('-f', '--field', action='store', type=str, default='FFT', help='HDF5-field')
    parser.add_argument('-o', '--output
