import weakref
import os
import gtk
import gobject

from sugar import environment


# §SUGAR_BUNDLE_PATH is the path to the activity bundle
# so we can use it to get the path to the default activity icon
_BUNDLE_PATH = os.environ.get('SUGAR_BUNDLE_PATH')

if _BUNDLE_PATH:
    _ICON_PATH = os.path.join(_BUNDLE_PATH, 'activity', 'activity-icon.svg')
else:
    _ICON_PATH = os.path.join(environment.get_bundle_path(),
                              'activity', 'activity-icon.svg')


class CanvasItem(gtk.DrawingArea):
    """
    CanvasItem represents a basic visual element of the Activity.
    CanvasItem provides a gtk.DrawingArea with a coordinate system that
    maps to the top-left corner of the gtk.DrawingArea and may scale
    the coordinates to zoom in/out of the view.
    """

    def __init__
