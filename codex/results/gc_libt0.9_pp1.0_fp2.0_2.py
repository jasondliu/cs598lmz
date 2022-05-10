import gc, weakref, sys

import pygst
pygst.require("0.10")
import gst

from kiwi.environ import environ
environ.add_resource("pixmaps", os.path.dirname(__file__))

grand_parent = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def escape_pango(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class GstPlayer(object):
    """
    This is the Gstreamer based player.
    """
    # pylint: disable=R0903,R0904
    #         Too few public methods
    #         Too many public methods

    __metaclass__ = Singleton
    # These are instances signals that are generated when a GStreamer
    # element emits them.  We will have to subscribe to the signals when
    # we create the hook.
    _signals = ["async-done", "track-info",
