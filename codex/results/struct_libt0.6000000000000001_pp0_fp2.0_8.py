import _struct
import types
import sys


class H264Decoder:
    def __init__(self):
        self.decoder = _ffi.new("H264DecoderContext *")
        self.decoder.width = 0
        self.decoder.height = 0

        self.frame = _ffi.new("H264Frame *")
        self.frame.width = 0
        self.frame.height = 0
        self.frame.data = _ffi.new("char[]", 0)

        self.buffer = _ffi.new("H264Buffer *")
        self.buffer.data = _ffi.new("char[]", 0)

    def decode(self, data):
        self.buffer.data = data
        self.buffer.size = len(data)
        self.buffer.pos = 0
        self.buffer.end = 0
        self.buffer.last_start_code = 0

        if not h264_decode_frame(self.decoder, self.frame, self.buffer):
            return None

        # need to copy data because it points to a
