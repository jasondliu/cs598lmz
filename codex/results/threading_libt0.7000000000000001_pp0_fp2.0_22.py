import threading
threading.stack_size(67108864)

# para evitar el problema de "permission denied"
# chmod +x get-pip.py
# sudo -H ./get-pip.py

# sudo -H python3.6 -m pip install numpy
# sudo -H python3.6 -m pip install scipy
# sudo -H python3.6 -m pip install scikit-image
# sudo -H python3.6 -m pip install scikit-learn
#sudo -H python3.6 -m pip install pydotplus
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import sklearn as sk
import skimage as ski
import time
import os
import sys
import glob
import string
import shutil

#from scipy import misc
import imageio

#from scipy.ndimage import imread
#from scipy.ndimage import imsave

#from skimage import io
#from skimage import data

#from sklearn.model_selection import train_
