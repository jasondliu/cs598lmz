import _struct
import struct
import wave
import pyaudio

# Variables for wave file (replace with your own)
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 0.01

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
print("finished recording")

filename = "file.wav"

# open the file for writing
wf = wave.open(filename, 'wb')

# set the channels
wf.setnchannels(CHANNELS)

