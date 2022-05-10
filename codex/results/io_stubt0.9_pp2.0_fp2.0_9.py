import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import cc3d.twedit5.twedit.utils.global_imports
f = cc3d.twedit5.twedit.utils.global_imports.GlobalImportsPlugin(view)
f.init()
f.parse()
