import gc, weakref
import numpy as np
from numpy.lib.stride_tricks import as_strided
from scipy.ndimage import map_coordinates
from scipy.spatial import KDTree
from scipy.misc import imread
from scipy.stats import multivariate_normal
from skimage.feature import blob_dog, blob_log
from skimage.filters import threshold_otsu
from skimage.util import img_as_ubyte
from skimage.restoration import denoise_tv_chambolle
from skimage.measure import label
from skimage.morphology import remove_small_objects, remove_small_holes
from skimage.measure import regionprops
from skimage.draw import circle_perimeter
from skimage.color import label2rgb
from skimage.feature import peak_local_max
from skimage.filters import threshold_otsu
from skimage.measure import label
from skimage.color import label2rgb
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
