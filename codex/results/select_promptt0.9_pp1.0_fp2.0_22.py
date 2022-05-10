import select
# Test select.select with zombied child (Issue 9182).
import subprocess
import sys
import time
p = subprocess.Popen((sys.executable, '-c', 'open("/dev/null").read()'))
read_fd, write_fd = os.pipe()
while p.poll() is None:
    select.select([read_fd], [], [], 1)
cpu_count = multiprocessing.cpu_count()
# Issue 10205: handle pathological cases
multiprocessing.set_executable(None)
if sys.platform == 'win32':
    multiprocessing.set_executable('notepad.exe')
else:
    multiprocessing.set_executable('/bin/ls')
multiprocessing.freeze_support()
multiprocessing.set_executable(None)
# Issue10478: ensure that freeze_support() doesn't break on Windows if
# sys.frozen is true.
multiprocessing.freeze_support()
sys.exit(0)
