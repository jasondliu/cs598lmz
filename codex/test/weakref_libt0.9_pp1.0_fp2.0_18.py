import weakref
from encdec.utils import export
from .components import *
from .operation import *

@export
class PlaceHolder (Operator):
  """A placeholder that can be used to receive a value.
  Args:
    name: A string that identifies which placeholder holds this value.
    graph: A reference to the current graph.
    shape: The shape of the placeholder.
    default_value: This value is used to initialize the placeholder when it is not
      provided.
    has_output_nodes: Whether this placeholder has output nodes. Assuming that if it
      is an input placeholder, then it is a graph input and no output node is
      created. Otherwise the output node is created, to allow easier calculations
      in the graph staging.
    input_sensor: An input sensor that further informs the placeholder about the
      shape of the input.
  """

  type = "placeholder"
  shape = None
  default_value = None
  input_sensor = None

