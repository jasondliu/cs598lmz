import weakref

from kivy.logger import Logger
from kivy.clock import Clock
from kivy.compat import PY2

# list of all the files currently opened by the GStreamer backend
_files = []

if PY2:
    import Queue as queue
else:
    import queue


class GstBuffer(object):

    def __init__(self, gstbuffer, caps, segment, duration, timestamp,
                 offset, offset_end, offset_end_time, flags, taglist,
                 config, context):
        self.gstbuffer = gstbuffer
        self.caps = caps
        self.segment = segment
        self.duration = duration
        self.timestamp = timestamp

        self.offset = offset
        self.offset_end = offset_end
        self.offset_end_time = offset_end_time

        self.flags = flags
        self.taglist = taglist
        self.config = config
        self.context = context

    def __repr__(self):
        return '<GstBuffer size=%d
