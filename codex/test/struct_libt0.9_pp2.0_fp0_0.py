import _struct
from io import BytesIO
import sys

from objects import *
from enums import *
from util import *

# Represents an object chain within a layout file.
#
# These are the things that store all the information
# necessary to draw a level in the game, for example:
#   tilesets, backgrounds, and more.
class LayoutObjectNode(object):
  def __init__(self, name, instance_count, parent_nodes):
    self.name = name
    self.instance_count = instance_count
    self.instances = {}
    self.parent_nodes = parent_nodes
    self.is_background = False
    self.is_autoscroll = False
    self.type = None

  def export(self, output):
    output.write('\n\n{name}\n'.format(name=self.name))
