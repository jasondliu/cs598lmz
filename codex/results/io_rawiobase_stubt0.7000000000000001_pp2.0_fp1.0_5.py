import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.buffer = None
        self.buffer_offset = None
        self.buffer_size = None
        self.buffer_is_read = None
        self.buffer_is_dirty = None
        self.file_pos = None
        self.closed = False
        self.mode_append = mode == "a"
        self.mode_write = mode in {"w", "a", "x"}
        self.mode_binary = mode.endswith("b")
        self.mode_text = mode.startswith("r") and not self.mode_binary
        self.mode_reading = self.mode_text or mode == "r"
        self.mode_updating = mode in {"r+", "w+", "a+", "x+"}
        self.mode_exclusive = mode in {"x", "x+"}
        self.mode_plus = mode[-1] == "+"
        self.mode_access = mode
