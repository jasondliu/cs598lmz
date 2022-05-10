import mmap
import numpy as np
import os
import os.path
import random
import re
import sys
import tarfile
import tqdm
import zipfile

import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants

from six.moves import urllib
from six.moves import xrange

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

# pylint: disable=unused-import
from tensorflow.contrib.framework.python.ops import audio_ops as contrib_audio
# pylint: enable=unused-import

from pydub import AudioSegment
from pydub.utils import make_chunks

from scipy.io import wavfile
from scipy import signal
from scipy.io.wavfile import write

import speech_data
