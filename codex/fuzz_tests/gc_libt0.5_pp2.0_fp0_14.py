import gc, weakref

import numpy as np
from numpy.testing import assert_array_equal

from skimage.util import img_as_float
from skimage.data import astronaut
from skimage.filter import canny, sobel, scharr, prewitt, roberts, hsobel, vsobel
from skimage.filter.rank import median
from skimage.filter.rank import mean_bilateral
from skimage.filter.rank import mean_percentile
from skimage.filter.rank import gradient
from skimage.filter.rank import enhance_contrast
from skimage.filter.rank import enhance_contrast_percentile
from skimage.filter.rank import enhance_contrast_bilateral
from skimage.filter.rank import maximum_filter, minimum_filter
from skimage.filter.rank import modal_filter
from skimage.filter.rank import threshold
from skimage.filter.rank import otsu
from skimage.filter.rank import try_all_threshold
from skimage.filter.rank import bottomhat
from skimage.filter.rank import tophat
from skimage
