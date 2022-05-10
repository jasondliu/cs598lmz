import ctypes
ctypes.cast(pBuffer, ctypes.POINTER(ctypes.c_float))

#%%
#https://github.com/mikeboers/PyAV/blob/master/demos/video_decode.py
import av
import av.datasets

container = av.open(r'D:\Users\njm\Documents\python\Videos\test.mp4')

#%%
#https://github.com/mikeboers/PyAV/blob/master/demos/video_decode.py

# Find the first video stream.
video_stream = next((s for s in container.streams if s.type == b'video'), None)
if video_stream is None:
    raise Exception('No video stream found!')

# Find the first audio stream.
audio_stream = next((s for s in container.streams if s.type == b'audio'), None)
if audio_stream is None:
    raise Exception('No audio stream found!')

# Instantiate a video frame and a video picture.
frame = video_stream.frame
picture
