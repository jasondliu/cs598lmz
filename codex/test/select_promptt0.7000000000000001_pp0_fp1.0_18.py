import select
# Test select.select() with a simple pipe

# Make sure we're using a known encoding.
import locale
locale.setlocale(locale.LC_ALL, "C")

import subprocess
args = ["/bin/sh", "-c", "echo foo"]
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check that select won't hang
r, w, x = select.select([p.stdout], [], [], 0)
print(r)
