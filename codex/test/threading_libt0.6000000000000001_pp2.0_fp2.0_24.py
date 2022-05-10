import threading
threading._DummyThread._Thread__stop = lambda x: 42

import gc
gc.disable()

import urllib2
urllib2.urlopen = lambda x: x

import pdb
pdb.set_trace = lambda: 42

import urllib
urllib.urlopen = lambda x: x

import imageop
imageop.scale = lambda x, y, z: x
imageop.grayscale = lambda x: x
imageop.invert = lambda x: x
imageop.crop = lambda x, y, z, w, v, u: x
imageop.scale2x = lambda x: x
imageop.offset = lambda x, y, z, w: x
imageop.scale2x = lambda x: x
imageop.offset2x = lambda x, y, z: x
imageop.scale3x = lambda x: x
imageop.offset3x = lambda x, y, z: x
imageop.offset4x = lambda x, y, z: x
imageop.offset5x = lambda x, y, z: x
