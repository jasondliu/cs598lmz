import lzma
lzma.open('111.txt.xz')
!ls -l *.xz

!pip3 show nltk
!pip3 show numpy

!python3 -V
!echo "hello world" > helloworld.txt
!cat helloworld.txt
!rm -r helloworld.txt
 
!ls -l > list.txt
!cat list.txt

!python3 > script.py <<EOF
print('hello world')
EOF

!cat script.py

#def lala():
#  print('hello')

#lala()

def add(a, b):
  return a + b

def test_add():
  assert add(2, 3) == 5
  assert add('space', 'ship') == 'spaceship'

test_add()

!python3 -m unittest -v script
 
#!/usr/bin/python3

from __future__ import print_function

import os.path
from io import BytesIO
import numpy as np
from functools import partial
