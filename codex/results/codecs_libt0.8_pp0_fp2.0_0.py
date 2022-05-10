import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# ---------------------------------------------------------------------------------------------------------------------
#%% Imports


import cv2
import numpy as np
import os.path
import pickle
import time

from pathlib import Path

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt

from local.lib.common.feedback import print_time_taken_ms
from local.lib.ui_utils.display_specification import Display_Window_Specification
from local.lib.ui_utils.local_ui.windows_base import Simple_Window

from local.configurables.externals.calibration import Reference_Calibration_Controller
from local.configurables.externals.calibration._helper_functions import calibration_segment_data
from local.configurables.externals.calibration._drawing_helpers import (draw_guidance_background,
                                                                        draw_overlay_background,
                                                                        draw
