import _struct

class jpeg_hdr(object):
    """
    A class to parse jpeg headers
    """
    def __init__(self, buf):
        """
        Constructor.
        @param buf: The buffer to parse.
        """
        self.buf = buf
        self.segments = []
        self.parse_header()

    def parse_header(self):
        """
        Parse the header.
        """
        self.parse_start_of_image()
        self.parse_segments()

    def parse_start_of_image(self):
        """
        Parse the start of image marker.
        """
        if self.buf[0:2] != "\xFF\xD8":
            raise Exception("Invalid start of image marker")

    def parse_segments(self):
        """
        Parse the segments in the buffer.
        """
        buf = self.buf[2:]
        while len(buf) > 4:
            type, length, buf = self.parse_segment(buf)
            self.segments.
