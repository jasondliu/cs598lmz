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

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed
import gc; gc.collect()

# The buffer must not be freed before the file is closed

