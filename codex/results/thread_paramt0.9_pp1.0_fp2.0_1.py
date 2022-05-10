import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize(name, dataset, target_col=None, filter_cols=None):
    plt.figure(figsize=(14,6))
    if filter_cols != None:
        dataset = dataset.filter(filter_cols, axis=1)
    
    
    graph = sns.pairplot(dataset, hue=target_col)
    plt.show()
    display(HTML('<a href="#">back to top^</a>'))
    return graph
 

def scatterMatrix(dataset, filteredColumns=None, dropColumns=None):
    df = dataset
    
    if dropColumns != None:
        df = df.drop(dropColumns, axis=1)
    
    if filteredColumns != None:
        df = df.filter
