import gc, weakref
import re
import os
import sys

try:
    from urllib.request import pathname2url
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.error import URLError
    from urllib.parse import urljoin
except ImportError:
    from urllib import pathname2url
    from urllib2 import urlopen, HTTPError, URLError
    from urlparse import urljoin

def gtk_widget_destroy_and_free(widget, *args):
    if widget.parent is not None:
        widget.parent.remove(widget)
    widget.destroy()
    del widget

def get_ui_objects(uim, objects):
    return [uim.get_widget(name) for name in objects]

def get_image_dir():
    path = os.path.dirname(os.path.realpath(__file__))
    return path

