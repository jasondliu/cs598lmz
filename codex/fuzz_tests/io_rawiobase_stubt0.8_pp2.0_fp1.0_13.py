import io
class File(io.RawIOBase):
    def __init__(self,filename,mode):
        self.mode=mode
        self.name=filename
        self.closed=False
        if mode.startswith("r"):
            self.fh=io.open(self.name,mode)
        elif mode.startswith("w") or mode.startswith("a"):
            self.fh=io.BytesIO()
        else:
            raise ValueError("Unsupported file open mode %s"%mode)
    def close(self):
        if not self.closed:
            self.flush()
            if self.mode.startswith("w") or self.mode.startswith("a"):
                fh=io.open(self.name,"wb")
                fh.write(self.fh.getvalue())
                fh.close()
            elif self.mode.startswith("r"):
                self.fh.close()
            self.closed=True
    def readable(self):
        return self.mode.startswith("r")
    def writ
