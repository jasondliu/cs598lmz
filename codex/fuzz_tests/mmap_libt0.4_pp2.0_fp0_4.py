import mmap
import os
import struct
import sys
import threading
import time

import cv2
import numpy as np

from . import config
from . import image_utils
from . import input_utils
from . import utils

# The number of frames to collect before writing a video file
FRAMES_PER_VIDEO = config.get('frames_per_video')

# The number of frames to collect before writing a video file
FRAMES_PER_IMAGE = config.get('frames_per_image')

# The number of seconds to wait between writing files
WRITE_INTERVAL = config.get('write_interval')

# The minimum number of seconds to wait between writing files
MIN_WRITE_INTERVAL = config.get('min_write_interval')

# The number of seconds to wait between writing files
WRITE_DELAY = config.get('write_delay')

# The number of seconds to wait between writing files
WRITE_DELAY_MAX = config.get('write_delay_max')

# The number of seconds to wait between writing files
WRITE
