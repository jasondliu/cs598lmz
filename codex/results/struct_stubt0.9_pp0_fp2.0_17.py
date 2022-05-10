from _struct import Struct
s = Struct.__new__(Struct)
s.endian = 1
s.format = "<ff"
s.size = s.calcsize(s.format)

__builtins__["open"] = lambda *args, **kwargs: None

def get_input():
    raw_frames = sys.stdin.read()
    frames = []

    for i in range(len(raw_frames)/8):
        frames.append(s.unpack_from(raw_frames, i*8))

    return frames

def process():
    frames_in = get_input()
    frames_out = []

    for i in range(len(frames_in)):
        frames_out.append(frames_in[i][0]*8.3)
        frames_out.append(frames_in[i][1]*8.3)

while True:
    process()
