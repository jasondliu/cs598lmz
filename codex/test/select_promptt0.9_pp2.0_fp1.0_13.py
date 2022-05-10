import select
# Test select.select()
import time

# This can be use for reading the data from a file, but that won't be a real-time recording data and not using USB
# from pyaudio import PyAudio, paInt16
# import numpy as np
# import wave
# import struct

def test_select():
    ready_to_read, ready_to_write, in_error = select.select([sys.stdin,], [sys.stdout,], [], 5)
    print(ready_to_read)
    print(ready_to_write)
    print('exited')
    sys.stdout.write('haha')
    #r = sys.stdin.readline()
    #print(r)

# def test_stdin():
#     r = sys.stdin.readline()
#     print(r)

# def test_wav():
#     wav_file = wave.open("./tmp/2.wav", "rb")
#     params = wav_file.getparams()
#     nchannels, sampwidth, framerate, nframes
