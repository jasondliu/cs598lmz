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

def check_files_content(content):
  return (check_file_content("/tmp/mmap_shared", content) and 
          check_file_content("/tmp/mmap_simulavr", content))

# check if we have a file name for mmap_demo.hex
if len(sys.argv) < 2:
  print("syntax: " + sys.argv[0] + " <path to mmap_demo.hex>")
  sys.exit(1)

# load the
