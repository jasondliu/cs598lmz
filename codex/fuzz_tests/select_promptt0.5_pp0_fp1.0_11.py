import select
# Test select.select()
#
# select() takes three lists of objects to monitor:
#   readable: objects that can be read from
#   writable: objects that can be written to
#   exceptional: objects with errors
#
# It returns three lists of objects that are ready for I/O:
#   readable: objects that can be read from
#   writable: objects that can be written to
#   exceptional: objects with errors
#
# If a list is empty, then it means that all objects in that list are ready.
#
# select() blocks until at least one of the objects is ready.
#
# select() is not supported on all platforms, and it may not be supported for
# all types of objects.

# select() takes three lists of objects to monitor:
#   readable: objects that can be read from
#   writable: objects that can be written to
#   exceptional: objects with errors
#
# It returns three lists of objects that are ready for I/O:
#   readable: objects that can be read from
#   writable: objects that can be written to
#   exceptional: objects with errors

