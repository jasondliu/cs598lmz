import selectors
import sys
import types

# A dictionary mapping file descriptors to sockets.
all_sockets = {}

# A dictionary mapping sockets to file descriptors.
all_fds = {}

# The maximum number of file descriptors that can be used.
max_fd = 0

# The maximum number of bytes that can be sent per write.
max_bytes_per_write = 4096

# The maximum number of bytes that can be received per read.
max_bytes_per_read = 4096

# A list of all sockets that are ready to be written to.
sockets_ready_to_write = []

# A list of all sockets that are ready to be read from.
sockets_ready_to_read = []

# A dictionary mapping socket objects to their current read buffers.
read_buffers = {}

# A dictionary mapping socket objects to their current write buffers.
write_buffers = {}

# A dictionary mapping socket objects to their current write offsets.
write_offsets = {}

# The selectors object.
selector = None

# A dictionary mapping file descriptors
