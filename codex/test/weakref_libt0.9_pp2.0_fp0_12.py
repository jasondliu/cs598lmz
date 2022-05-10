import weakref

from enum import Enum

class BadDim(Exception):
	pass

class NotUsable(Exception):
	pass

class Added(object):
	""" Special object to deliniate the postconditions of an operation."""
	pass

# 2 possible tags: index and flt.
class Tag(Enum):
	index = 1
	flt = 2

class MetaTag:
	""" A partial sum or a generated set of tags."""
	tag = Tag.index
	pair = "" # pair of tags.

class TagMap:
	def __init__(self):
		self.indexToPosn = {} # maps index to position in the generated list.
		self.posnToIndex = [] # maps position to index in the generated list
		self.fltToPosn = {} # maps filter to position in the generated list
		self.posnToTag = [] # maps position to filter in the generated list

	def __getitem__(self,k):
		"""Implements [tag] retrieval."""
