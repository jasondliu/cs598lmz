import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import sys
# sys.path.append("C:\\Users\\micha\\Documents\\GitHub\\SciPy-Tutorial-2019\\")
# sys.path.append("C:\\Users\\micha\\Documents\\GitHub\\SciPy-Tutorial-2019\\examples")

# from examples.segmentation import (morphological_chan_vese,
#                                    morphological_geodesic_active_contour,
#                                    morphological_chan_vese_inverse_gaussian,
#                                    morphological_geodesic_active_contour_inverse_gaussian)

# from skimage import data
# from skimage.util import img_as_float
# from skimage.filters import gabor_kernel

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import ndimage as ndi

# from skimage.color import rgb2gray

