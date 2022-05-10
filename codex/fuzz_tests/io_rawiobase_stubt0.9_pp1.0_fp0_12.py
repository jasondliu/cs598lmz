import io
class File(io.RawIOBase):
    def __init__(self, uid):
        self.fid = os.open(uid, os.O_RDONLY)
    def readinto(self, b):
        return os.read(self.fid, b)
    def close(self):
        os.close(self.fid)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
with File("junk") as file_obj:
    print(file_obj.readinto(3))

with open("hakan.txt", "w") as f:
    print("h", end="", file=f)
from contextlib import AbstractContextManager
class EseIde(AbstractContextManager):
    def __enter__(self):
        print("yaz cikti")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("mehmet abi")
with EseIde():
    print("i am a chef")
def cow(n):
    print(n,
