import select
import socket
import sys
import time

import numpy as np
import pyaudio

from pylsl import StreamInfo, StreamOutlet, local_clock

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)

info = StreamInfo('BioSemi', 'EEG', 8, 100, 'float32', 'myuid34234')

# next make an outlet
outlet = StreamOutlet(info)

# open audio stream
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = np.fromstring(in_data, dtype=np.float32)
    outlet.push_sample(data, local_clock())
