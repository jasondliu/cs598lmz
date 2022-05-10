import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import v_measure_score

from sklearn.mixture import GaussianMixture

from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

from sklearn.cluster import Birch

from sklearn.cluster import SpectralClustering

from sklearn.cluster import MeanShift

from sklearn.cluster import AffinityPropagation

from sklearn.cluster import OPTICS

from sklearn.cluster import FeatureAgglomeration

from sklearn
