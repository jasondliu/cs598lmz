import select
import sys
import time
import termios
import tty
# import os

import numpy as np
from PIL import Image
from pybullet_envs.bullet.kukaGymEnv import KukaGymEnv


def get_image():
    image_data = vrep.simxGetVisionSensorImage(clientID, vision_sensor, 0, vrep.simx_opmode_buffer)
    if len(image_data) > 0:
        img = Image.fromarray(np.array(image_data[2], dtype=np.uint8))
        img = np.array(img.resize((84, 84)))
        return img
    else:
        print('no image data received')


def _kbhit():
    '''
    Returns True if keyboard character was hit, False otherwise.
    '''
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3]
