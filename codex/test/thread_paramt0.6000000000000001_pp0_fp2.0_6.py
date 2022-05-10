import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
#%%
# #%%
# from IPython.core.debugger import set_trace
# from matplotlib import pyplot as plt
# from scipy.io import loadmat
# from sklearn import metrics
# import h5py
# import numpy as np
# import os
# import pandas as pd
# import sys
# import tensorflow as tf

# #%%
# # Set PATHs
# #curr_dir = '/home/jovyan/shared/InteliRad-gasper'
# curr_dir = os.getcwd()
# PATH_DATA = os.path.join(curr_dir, 'DATA')
# PATH_WORK = os.path.join(curr_dir, 'WORK')
# PATH_MODEL = os.path.join(curr_dir, 'MODEL')
# PATH_VAL = os.path.join(curr_dir, 'VAL')

# #%%
# # Load labels
# df
