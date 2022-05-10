import gc, weakref
import numpy as np

class MyObj(object):
    def __init__(self):
        x = np.zeros((100,10))
        x = 1.0
