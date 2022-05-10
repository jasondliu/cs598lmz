fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# [Errno 36] File name too long
import os
os.mkdir(b'a' * 256)

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 13] Permission denied
import os
os.mkdir(b'.')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
os.mkdir(b'\x00')

# [Errno 22] Invalid argument
import os
