import ctypes
ctypes.cdll.LoadLibrary("/usr/local/lib/libgcc_s.so.1")
ctypes.cdll.LoadLibrary("/usr/local/lib/libstdc++.so.6")

import sys
sys.path.insert(1,'/usr/local/lib/python3.5/site-packages')
sys.path.append('/usr/local/lib/python3.5/site-packages/scipy')
sys.path.append('/usr/local/lib/python3.5/site-packages/sklearn')
sys.path.append('/usr/local/lib/python3.5/site-packages/skimage')
sys.path.append('/usr/local/lib/python3.5/site-packages/skimage/io')
sys.path.append('/usr/local/lib/python3.5/site-packages/skimage/color')
sys.path.append('/usr/local/lib/python3.5/site-packages/skimage/transform')
sys.path.append('/usr/local/lib/
