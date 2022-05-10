import socket
# Test socket.if_indextoname()
#
# This test is intended to be run on a system with two interfaces, one
# of which is named "lo" and the other is named something else.
#
# The test will fail if the system has only one interface, or if the
# system has more than two interfaces, or if the system has two
# interfaces but neither is named "lo".

if_name = socket.if_indextoname(1)
if if_name != 'lo':
    raise SystemExit('FAIL: socket.if_indextoname(1) returned %r, not "lo"'
                     % if_name)
print('PASS: socket.if_indextoname(1) returned "lo"')

if_name = socket.if_indextoname(2)
if if_name == 'lo':
    raise SystemExit('FAIL: socket.if_indextoname(2) returned "lo", not '
                     'something else')
print('PASS: socket.if_indextoname(2) returned something other than "lo"')
