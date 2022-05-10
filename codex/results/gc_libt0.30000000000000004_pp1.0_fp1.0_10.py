import gc, weakref
from operator import attrgetter

from . import _curses
from . import _curses_panel

# -----------------------------------------------------------------------------

def _get_panel_list():
    """Return a list of all panels in the order that they should be displayed
    on the screen.
    """
    panels = []
    for panel in _curses_panel.top_panel():
        while panel:
            panels.append(panel)
            panel = panel.below()
    return panels

def _update_panels():
    """Update the curses panels.
    """
    # Get the list of panels in the order that they should be displayed.
    panels = _get_panel_list()

    # Update the panels.
    for panel in panels:
        panel.update_scr_win()

    # Display the panels.
    _curses_panel.update_panels()

# -----------------------------------------------------------------------------

class Panel(object):
    """A panel is a window that can be moved around the screen.
    """
    def __init__(self, window):
        """Create a panel.

       
