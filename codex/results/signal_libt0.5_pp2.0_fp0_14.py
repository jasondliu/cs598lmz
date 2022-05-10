import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# this is needed to avoid segmentation fault
# when using matplotlib's imshow function
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

import sys
sys.path.append('../')
from utils import *

def main():
    """
    Load the data, perform k-means clustering, and save the
    cluster assignments as a csv file.
    """
    # Load the data
    X = load_data()

    # Run k-means clustering with k = 50
    kmeans = KMeans(n_clusters=50, random_state=0).fit(X)

    # Save the cluster assignments
    np.savetxt('kmeans_assignments.csv', kmeans.labels_, fmt='%d')

if __name__ == '__main__':
    main()
