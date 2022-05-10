import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\r" + " " * 50 + "\r")).start()

# Import various dependencies.
import glob
import matplotlib.pyplot as plt
import numpy as np
import os
#import PIL
import tensorflow as tf
#from tensorflow.python import debug as tf_debug

# Allow image embeding in notebook.
#%matplotlib inline

# Functions for loading caption data
def get_captions_for_fns(fns, cap_map_file_name, data_dir='data'):
    """Load captions for a given set of filenames"""
    if not os.path.isfile(data_dir+'/caps/'+cap_map_file_name+'.npy'):
        print("Caption mapping for {} not found.".format(cap_map_file_name))
        sys.exit(1)
    cap_map = np.load(data_dir+'/caps/'+cap_map_file_name+'.npy', encoding = 'latin1').item()
    f
