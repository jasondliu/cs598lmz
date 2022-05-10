from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, memlimit=None, filters=None)
print("lzma_decompress success")

# scipy
import numpy as np
import scipy as sp
import scipy.optimize
import scipy.ndimage
print("scipy success")

# skimage
import skimage as sk
import skimage.io
import skimage.io.collection
import skimage.io.manage_plugins
import skimage.transform
import skimage.util
import skimage.color
import skimage.restoration
import skimage.morphology
import skimage.segmentation
print("skimage success")

# sklearn
import sklearn
import sklearn.cluster
import sklearn.decomposition
import sklearn.datasets
import sklearn.ensemble
import sklearn.feature_extraction
print("sklearn success")
import sklearn.utils
print("sklearn.utils success")

# skvideo
import skvideo.io
print("skvideo success")

# tqdm
import tqdm
print
