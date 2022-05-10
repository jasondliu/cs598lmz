import io
# Test io.RawIOBase()
init_pyfile = io.RawIOBase()
import io
# Test io.RawIOBase.seekable()
init_pyfile.seekable()
import io
# Test io.RawIOBase.readable()
init_pyfile.readable()
import io
# Test io.RawIOBase.writeable()
init_pyfile.writeable()
import io
# Test io.RawIOBase.flush()
init_pyfile.flush()
import os
# Test os.path.join()
os.path.join('.', 'tests', 'init.py')
import subprocess
# Test subprocess.Popen()
subprocess.Popen('dir', shell=True)
import tempfile
# Test tempfile.NamedTemporaryFile()
init_fd = tempfile.NamedTemporaryFile(suffix='.py')
import random
# Test random.randint()
random.randint(0, 12)
