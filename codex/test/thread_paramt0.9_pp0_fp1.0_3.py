import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()
import os
from matplotlib import pylab
import pylab as pl
import seaborn as sns

from sklearn.cluster.bicluster import SpectralCoclustering
from sklearn.metrics import consensus_score



import pylab
import seaborn
from pylab import *
import matplotlib.pyplot as plt
import module_time_series as ts
import module_load_data as imd
import module_clustering as cl

with sns.axes_style("darkgrid"):
    pylab.figure(figsize=(15, 8))
    pylab.axes([0.045,0.045,0.93,0.93])

#load the data set
data_file = "../sample_data/clustering/test_data_iris.txt"
dataset = pd.read_csv(data_file)
dataset = dataset.drop(['species'], axis=1)
