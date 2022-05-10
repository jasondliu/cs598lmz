import mmap
from PIL import Image
from tqdm import tqdm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
import cv2
from sklearn.metrics import pairwise
import scipy.stats
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
import matplotlib.cm as cm
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import calinski_harabasz_score


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def
