from bz2 import BZ2Decompressor
BZ2Decompressor()
#if mpl is installed.
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import numpy as np
#import os

filename = './FaceData/Yale_32x32.mat'
import h5py
import numpy as np
with h5py.File(filename, 'r') as f:
    a=f['fea'].value
    print(a)
    print(a.shape)
print(a[0].shape)

#a[0].reshape((32, 32))
a[1].shape

list = [0, 9, 29, 49]
import scipy.misc
for item in list:
    scipy.misc.imsave('c'+str(item)+'.png', a[item].reshape((32, 32)).transpose())

%matplotlib inline

fname = './FaceData/c0.png'
img = cv2.imread(fname)
dst = cv2.fastNlMeansDenoisingColored
