import weakref

import numpy as np

from .node import Node
from .node_parameters import Node_Parameters
from .node_draw import Node_Draw
from .node_inputs import Node_Inputs
from .node_outputs import Node_Outputs

class Node_Distributor(Node):
	node_info = {
		"label" : "Distributor",
		"description" : "Distributes input along a list of outputs.",
		"inputs" : (
			Node_Inputs("input"),
		),
		"outputs" : (
			Node_Outputs("output"),
		),
		"buttons" : (),
		"path" : {
			"widget" : Node_Path_Widget,
			"signal" : "path_changed",
			"sender" : "self",
		},
	}

	def __init__(self):
		super(Node_Distributor, self).__init__()

		self.out_values = np.
