import select
# Test select.select() in non-blocking mode
# (This runs forever, use control-c to kill it.)
#
# Usage:
#    python select_timeout.py [n]
#
# Where n is an optional argument specifying the number of file
# descriptors to monitor.  The default is 5.

N = 10
if len(sys.argv) > 1:
    N = int(sys.argv[1])

