import gc, weakref
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
import skimage
from skimage import data, io, filters
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.color import rgb2gray
from skimage.feature import ORB, match_descriptors, corner_harris, corner_peaks, plot_matches
from skimage.measure import ransac
from skimage.transform import ProjectiveTransform, FundamentalMatrixTransform, EssentialMatrixTransform
from skimage.exposure import equalize_hist
from skimage.filters import gaussian, sobel, laplace, frangi, hessian, prewitt
from skimage.feature import canny
from skimage.segmentation import active_contour
from skimage.morphology import binary_dilation, binary_erosion, binary_closing
from skimage.measure import label, regionprops
from skimage.transform import hough_line_peaks, hough_line, hough_circle, hough_circle_pe
