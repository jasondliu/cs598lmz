import mmap
import sys
import io
import os
import json

#------------------------------------------------------------------------------
# SOF Handling
#------------------------------------------------------------------------------

def get_sof(filepath):
    # Get the size of the file in bytes
    file_size = os.path.getsize(filepath)

    # Open the file in read only mode
    file_object  = open(filepath, "rb")
    f = mmap.mmap(file_object.fileno(), 0, access=mmap.ACCESS_READ)
    sof = bytearray()

    # Search for the SOF header
    for i in range(0, file_size):
        if f[i] == 0xFF and f[i+1] >= 0xC0 and f[i+1] <= 0xC3:
            # Found the SOF header. Get all the data up to the next marker.
            for j in range(i+2, i + f[i+2] * 256 + f[i+3]):
                sof.append(f[j])
            break

    # Close the file

