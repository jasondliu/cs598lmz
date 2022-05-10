import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import xdot
import time

XY_SCALING_FACTOR = 1.5

def to_float(val):
  if isinstance(val, float):
    return val
  elif isinstance(val, str):
    return float(val)
  else:
    assert False, 'Must be str, float or int.'

class Graph(xdot.DotWidget):
  def __init__(self, title, graph_data):
    self.title = title
    self.data = graph_data
    self.selected_node = None
    self.view_state = 0 # 0 = sum node view, 1 = sum edge view
    xdot.DotWidget.__init__(self)
    self.set_filter('fdp')

  def handle_key_press_event(self, event):
    key = gtk.gdk.keyval_name(event.keyval)
    if key == 'Escape':
      gtk.main_quit()
   
