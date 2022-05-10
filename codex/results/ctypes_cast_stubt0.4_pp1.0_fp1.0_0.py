import ctypes
ctypes.cast(0, ctypes.py_object)

# Import the PyBindGen generated module.
from pybindgen import *

# Import the module we're testing.
import gst

# Import the type map module.
import pygst_type_map

# Create an instance of the Gst.Object type.
obj = gst.ElementFactory.make("fakesrc", "source")

# Create an instance of the Gst.Buffer type.
buf = gst.Buffer()

# Create an instance of the Gst.Caps type.
caps = gst.Caps("video/x-raw-yuv")

# Create an instance of the Gst.Structure type.
struct = gst.Structure("video/x-raw-yuv")

# Create an instance of the Gst.TagList type.
taglist = gst.TagList()

# Create an instance of the Gst.TagSetter type.
tagsetter = gst.ElementFactory.make("fakesrc", "source")

# Create an instance of the Gst.Pad type.

