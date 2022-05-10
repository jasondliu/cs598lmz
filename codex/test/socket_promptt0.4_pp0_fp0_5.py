import socket
# Test socket.if_indextoname()
#
# This test is intended to be run from the Linux buildbot.
#
# It attempts to find the interface index for eth0, and then
# converts that index back to a name.
#
# If this test fails, then it is likely that the Linux kernel
# does not have the necessary support for if_indextoname().
#
# This test will be skipped if the Linux kernel is too old
# to support if_indextoname().

if_name = 'eth0'

if_index = socket.if_nametoindex(if_name)

if_name2 = socket.if_indextoname(if_index)

