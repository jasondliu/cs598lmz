import socket
# Test socket.if_indextoname()

print socket.if_indextoname(1)
"""

    test.run(arguments = '.', 
             stderr = None, 
             status = 0)

    test.pass_test()

# test the "socket" module
test.subdir('socket')

test.write('socket/__init__.py', "")

test.write('socket/socket.py', """\
import sys
import socket
# Test socket.if_indextoname()

print socket.if_indextoname(1)
""")

test.write('socket/SConscript', """\
Import("env")
env.LoadToolScript("../tool.py")
""")

test.run(arguments = '.', 
         stderr = None, 
         status = 0)

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
