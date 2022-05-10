import mmap
import numpy as np
import struct
import subprocess
import sys
import tempfile

from scipy.io import wavfile

from aubio import source, onset, pitch, tempo, pvoc, cvec

from aubio.utils import vec2string

# Parameters

# Number of seconds to run for
duration = 5

# Number of seconds to run for
framerate = 44100

# Number of seconds to run for
hop_s = 512

# Number of seconds to run for
framesize = hop_s * 4

# Number of seconds to run for
samplerate = 44100

# Number of seconds to run for
channels = 1

# Number of seconds to run for
min_pitch = 55

# Number of seconds to run for
max_pitch = 2000

# Number of seconds to run for
buf_size = 2048
