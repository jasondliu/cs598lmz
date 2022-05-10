import select
# Test select.select()
#
# Note: select() is not supported on all platforms!
#
# On Linux 2.6.11.4 (Fedora Core 4), it works for pipes but
# not for plain files.
#
# On Solaris 9 (SunOS 5.9), it works for pipes and sockets but
# gives bogus results for plain files

import os, sys, time

