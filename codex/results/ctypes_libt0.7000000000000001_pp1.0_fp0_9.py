import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial.transform import Rotation as R

def quat_to_euler(q):
    q = q / np.linalg.norm(q)
    euler = R.from_quat(q).as_euler('zyx', degrees=False)
    return euler

def euler_to_quat(euler):
    return R.from_euler('zyx', euler, degrees=False).as_quat()

class Human(object):
    def __init__(self):
        self.pos = (0,0,0)
        self.rot = (0,0,0)
        self.vel = (0,0,0)
        self.quat = euler_to_quat(self.rot)

    def update(self, dt):
        self.pos += self.vel * dt

    def get_pos(self):
        return
