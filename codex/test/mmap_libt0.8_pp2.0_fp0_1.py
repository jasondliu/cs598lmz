import mmap
import numpy as np
import time

class Pupil:
    def __init__(self, record_path, fps=60, min_radius=5, max_radius=70,
                 delta=5, bl_size=301, thresh=0.13, eq_hist=True,
                 t_min=0, t_max=1, blur_size=5, blur_sigma=2,
                 method=cv2.TM_CCOEFF_NORMED):
        self.record_path = record_path
        self.fps = fps
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.delta = delta
        self.bl = bl_size
        self.thresh = thresh
        self.eq_hist = eq_hist
