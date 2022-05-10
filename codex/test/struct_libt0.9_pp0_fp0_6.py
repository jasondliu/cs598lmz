import _struct
import cStringIO

HEADER_SIZE = 0x3C

def get_resource():
    return { "version" : "0.0.1", "fmt" : [ { "id" : "icon", "description" : "Icon format (.ico)", "mime" : "image/x-icon" } ] }

class ICON_DIR_ENTRY():
    def __init__(self, width=None, height=None, color_count=None, reserved=None, num_planes=None, bit_count=None):
        self.width = width
        self.height = height
        self.color_count = color_count
        self.reserved = reserved
        self.planes = num_planes
        self.bit_count = bit_count

