import mmap
import re
import subprocess
import os

# Read in the file
f = open('/proc/meminfo', 'r')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Look for the line that starts with 'MemFree'
memfree_re = re.compile(r'^MemFree:\s+(\d+)\skB')
m = memfree_re.search(s)

if m:
	memfree = m.group(1)
	print memfree
else:
	print "No match"

# Get the current swap usage
result = subprocess.Popen("swapon -s", shell=True, stdout=subprocess.PIPE).stdout.read()

print result

# Get the current swap usage
result = subprocess.Popen("swapon -s", shell=True, stdout=subprocess.PIPE).stdout.read()

print result

# Get the current swap usage
result = subprocess.Popen("swapon -s", shell=True
