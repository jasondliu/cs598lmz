import select
# Test select.select with all sending and receiving sockets.

# Should be run in a separate process by test_select.

import os
import select
allocator = __import__(os.environ["ALLOCATOR"])

# We use pipes to handle the SYNCH_OP, which works everywhere.
# The rest will work with sockets.

sockets = []
for socket_module in [allocator, socket]:
    for type in socket_module.SOCK_STREAM, socket_module.SOCK_DGRAM:
        for proto in socket_module.SOL_TCP, socket_module.SOL_UDP:
            s = socket_module.socket(socket_module.AF_INET, type, proto)
            # Invalid address
            try:
                s.connect(("{{invalid}}", 8888))
            except socket_module.gaierror:
                pass
            else:
                raise Exception("should have raised")

            s.bind(("0.0.0.0", 0))
            sockets.append(s)

from test import test_support

synch
