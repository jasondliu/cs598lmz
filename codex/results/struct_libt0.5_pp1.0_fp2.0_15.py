import _struct

#==============================================================================
# Constants
#==============================================================================

#==============================================================================
# Utility functions
#==============================================================================

#==============================================================================
# Classes
#==============================================================================

#------------------------------------------------------------------------------
class Chunk(object):
    #--------------------------------------------------------------------------
    def __init__(self, file_object, offset, parent=None):
        self.file_object = file_object
        self.offset = offset
        self.parent = parent
        self.children = []
        self.child_index = 0
        self.child_offset = 0
        self.child_count = 0

        self.read_header()

    #--------------------------------------------------------------------------
    def read_header(self):
        # Read the chunk header
        self.file_object.seek(self.offset)
        self.chunk_id, self.chunk_size = _struct.unpack('<4sI', self.file_object.read(8))

        # Read the chunk data
        self.file_object.seek(self.offset + 8)
        self.chunk_data = self.file_
