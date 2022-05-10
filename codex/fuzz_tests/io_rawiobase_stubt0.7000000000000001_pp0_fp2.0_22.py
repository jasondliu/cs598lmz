import io
class File(io.RawIOBase):
    def __init__(self):
        self.buffer = []
    def write(self, buf):
        self.buffer.append(buf)
        return len(buf)
    def read(self, size=-1):
        if size == -1:
            ret = b''.join(self.buffer)
            self.buffer = []
            return ret
        return self.buffer.pop(0)
</code>
Your example:
<code>import io
import sys
import pyaudio
chunk = 1024
wf = wave.open("music/test.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(chunk)

file = File()
stream.start_stream()
sys.stdout = file

while data != '':
    stream.write(data)
    data
