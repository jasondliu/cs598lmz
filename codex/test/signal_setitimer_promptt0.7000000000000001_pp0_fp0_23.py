import signal
# Test signal.setitimer()
# (see also 'man 2 setitimer')
#
# The following doesn't work yet (due to a bug in gdb.py):
#
# (gdb) break setitimer
# Function "setitimer" not defined.
# Make breakpoint pending on future shared library load? (y or [n]) y
# (gdb) c
# Continuing.
#
# Breakpoint 1, 0x00007ffff7bcb7c0 in setitimer () from /lib64/libc.so.6
# (gdb) bt
# #0  0x00007ffff7bcb7c0 in setitimer () from /lib64/libc.so.6
# #1  0x0000000000400902 in main () at a.c:26
# (gdb) ...and then Python just hangs.

# There is a bug in Fedora 20 that causes a Python crash when we enable this.
# See http://sourceware.org/bugzilla/show_bug.cgi?id=16549
required_kernels = ['2.6.32']

