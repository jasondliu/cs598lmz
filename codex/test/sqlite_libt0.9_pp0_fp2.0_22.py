import ctypes
import ctypes.util
import threading
import sqlite3
import shelve
import sys
import os

logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO)

# Bizarre: my Python doesn't find the ZODB pickle module unless
# I repeat this block exactly, even though sys.path already 
# includes /usr/lib/python2.7/site-packages.

db = shelve.open("spheres.shelve")

class Entity:
  
  # Each entity is a sphere with a radius, a polar angle, and an azimuth.

  def __init__(self, sphere, father_id=None, segment_id=None, feature_id=None, feature_type=None):
    self.sphere = sphere
    self.father_id = father_id
    self.segment_id = segment_id
