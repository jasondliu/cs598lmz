import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
from LucasKanade import LucasKanade

# write your script here, we recommend the above libraries for making your animation
if __name__ == '__main__':
    carseq = np.load('../data/carseq.npy')
    rect = np.array([59, 116, 145, 151])
    rects = np.zeros((carseq.shape[2], 4))
    rects[0] = rect
    for i in range(1, carseq.shape[2]):
        It = carseq[:, :, i - 1]
        It1 = carseq[:, :, i]
        p = LucasKanade(It, It1, rect)
        rect = rect + np.array([p[1], p[0], p[1], p[0]])
        rects[i] =
