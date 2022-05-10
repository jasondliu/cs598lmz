import bz2
bz2.__file__

bz2f = bz2.BZ2File('dsjtzs_txfz_training.txt.bz2', 'r')
output = open('dsjtzs_txfz_training.txt', 'w')
try:
    output.write(bz2f.read())
finally:
    output.close()
    bz2f.close()

import math
import numpy as np
import sklearn.metrics as metrics
import matplotlib
import matplotlib.pyplot as plt
from random import random
%matplotlib inline
matplotlib.style.use('ggplot')

# Helper function to plot a confusion matrix.
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm, interpolation='nearest', cmap=cmap
