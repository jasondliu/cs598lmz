import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_void_p)
FUNTYPE_C = ctypes.CFUNCTYPE(ctypes._CData, ctypes.c_void_p)

import os

def find_libs():
  '''Find libraries'''
  from subprocess import Popen, PIPE, check_output, CalledProcessError
  from os.path import dirname, isdir, join

  if isdir('/usr/lib64'):
    try:
      #this is for the old versions of NM
      libs = check_output(['nm', '-o']).split('\n')
      libs = [l.split()[-1] for l in libs]
      return [l for l in libs if l.startswith('/usr/lib64/')]
    except CalledProcessError:
      pass #this is for Ubuntu, NM is old
  elif isdir('/opt/local/lib'):
    return [os.path.join('/opt/local/lib', l) for l \
            in os
