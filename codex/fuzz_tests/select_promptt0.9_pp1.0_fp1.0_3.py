import select
# Test select.select
#
# Why use select ?
# If you have many file descriptors, and don't want to spin
# trying to .read() all of them, select() is an interface
# to the underlying OS handling of I/O (100% non-blocking) and
# will tell you which file descriptors have I/O ready and which
# ones don't. You issue a select command, wait a small amount of
# time, and then do I/O on the file descriptors that are ready.
#
#
# The cool thing about using select, is that you can use it for more
# than just file handles - it also works for pipes, sock fds, etc.
#
# The file handles can be anything - including a pipe or sock fd,
# even if it was opened in blocking mode.
#
# select only works on POSIX, not on Windows.
#
# select only handles the blocking calls - read and write.  It
# doesn't work with accept().
#
# To get the full advantages of select, you should use it with
# non-blocking I/O. If you declare your file handles as non
