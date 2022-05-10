import mmap
# Test mmap.mmap
with open('/tmp/foo','wb+') as f:
    mm=mmap.mmap(f.fileno(),0)
    mm.write('hello, python\n')
    mm[:5]='bye'
    f.seek(0)
    print f.read()
    mm.close()
    f.close()

import os
print os.path.abspath(__file__)

import os
import os.path

print os.path.dirname(__file__)
print os.path.abspath(os.path.dirname(__file__))

print os.path.dirname(os.path.abspath(__file__))

import os
import sys

file_path=os.path.abspath(__file__)
project_path=os.path.dirname(file_path)
sys.path.append(project_path)

import os
import sys

print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath
