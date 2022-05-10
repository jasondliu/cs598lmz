import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()

# using os.system
import os
os.system('echo -n "\a"')

# using winsound
import winsound
winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

# using subprocess
import subprocess
subprocess.Popen(['start', 'beep'], shell=True)

# using pyaudio
import math
import pyaudio
import wave

#define stream chunk
chunk = 1024

#open a wav format music
f = wave.open(r"beep-01a.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#play stream
