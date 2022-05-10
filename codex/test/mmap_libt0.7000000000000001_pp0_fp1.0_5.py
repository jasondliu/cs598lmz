import mmap
import numpy

from pysimulavr import *
from pysimulavr.demo.mmap_demo import mmap_demo

def check_file_content(fileName, content):
  f = open(fileName, "r")
  fileContent = f.read()
  f.close()
  if fileContent != content:
    print(fileName + " has wrong content!")
    print(fileContent)
    print("expected:")
    print(content)
    return False
  return True
