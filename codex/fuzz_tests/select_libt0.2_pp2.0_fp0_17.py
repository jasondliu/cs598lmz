import select
import socket
import sys
import time

import numpy as np

from . import _lib
from . import _util
from . import _video

# TODO:
# - Add support for the "video_size" parameter.
# - Add support for the "video_mjpeg" parameter.
# - Add support for the "video_channel" parameter.
# - Add support for the "video_bitrate" parameter.
# - Add support for the "video_rotation" parameter.
# - Add support for the "video_hflip" parameter.
# - Add support for the "video_vflip" parameter.
# - Add support for the "video_exposure_mode" parameter.
# - Add support for the "video_exposure_metering_mode" parameter.
# - Add support for the "video_exposure_compensation" parameter.
# - Add support for the "video_exposure_shutter_speed" parameter.
# - Add support for the "video_exposure_iso" parameter.
# - Add support for the "video_stabilization" parameter.
