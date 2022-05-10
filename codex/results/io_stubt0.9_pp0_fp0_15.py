import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # need to get rid of the buffer

%matplotlib inline
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')

plt.subplot(2, 2, 1)
plt.plot(view[0:960])

plt.subplot(2, 2, 2)
plt.plot(view[960:1920])

plt.subplot(2, 2, 3)
plt.plot(view[1920:2880])

plt.subplot(2, 2, 4)
plt.plot(view[2880:3840])

plt.show()

 

!screen -S yampp -p 0 -X stuff 'echo -e "quit\n" | nc localhost 8000\n'

# Currently the program just tries to trigger the alarm
# rather than actually parsing the time from the data

import os
import time
import sys
import math
import struct
import numpy
import matplotlib.
