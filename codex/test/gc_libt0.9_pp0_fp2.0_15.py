import gc, weakref
import random

class gpsNode:
	def __init__(self, gps, level=0, x=0, y=0, z=0, parent=None, child0=None, child1=None, child2=None, child3=None, child4=None, child5=None, child6=None, child7=None, treeType=0):
		self.gps = gps
		self.level = level
		self.x = x
		self.y = y
		self.z = z
		self.parent = parent
		self.child0 = child0 # -x +y +z
		self.child1 = child1 # +x +y +z
		self.child2 = child2 # +x -y +z
		self.child3 = child3 # -x -y +z
		self.child4 = child4 # -x +y -z
		self.child5 = child5 # +x +y -z
		self.child6 = child6 # +x -y -
