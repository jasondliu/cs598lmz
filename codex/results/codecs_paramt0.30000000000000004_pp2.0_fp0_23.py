import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import subprocess
import shutil
import tempfile
import time
import datetime
import traceback

import cv2
import numpy as np

import config
import util
import util_log

#
#
#

def get_video_info(video_file):
    cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', video_file]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('ffprobe failed: %s' % err)
    return json.loads(out)

def get_video_frame_count(video_file):
    info = get_video_info(video_file)
    return int(info['streams'][0]['nb_frames'
