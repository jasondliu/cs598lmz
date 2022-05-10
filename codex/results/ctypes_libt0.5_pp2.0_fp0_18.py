import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_core.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_imgproc.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_highgui.so')

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(image, title='Image'):
    plt.imshow(image)
    plt.title(title)
    plt.show()

def show_images(images, cols=1, titles=None):
    assert((titles is None)or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):

