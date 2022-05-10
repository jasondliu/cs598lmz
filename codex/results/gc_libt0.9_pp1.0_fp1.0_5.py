import gc, weakref, pickle
import types
import itertools

from vrml import node, field, prototypes
from vrml import mecom, serialisers
from vrml.prototypes import *
from vrml.mecom import *

def serialise( scene, out = sys.stdout ):
	walk( scene, out )
	out.write("\n")

# helper for walking a scene
def walk(
	scene, out, indent = 0,
	scriptRegistry = {}, specialRegistry = {},
	serialiser = serialisers.X3dSerialiser()
):
	def outNode(node):
		nodeType, nodeDef = node

		if isinstance(node, NodeClass):
			nodeType = node.nodeType
			nodeDef = node.nodeDef
		else:
			# Ensure we're derviving directly from a NodeClass
			# so that we can use the implicit nodeType
			nodeDef = PrototypeNode(nodeType, {})
			nodeType = nodeDef.nodeType
		
