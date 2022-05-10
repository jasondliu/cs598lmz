import select
# Test select.select()
# https://docs.python.org/3/library/select.html#select.select
# https://pymotw.com/2/select/

# select() can be used as a stand-alone function, or via the selectors module.
# - select() works on low-level file descriptors.
# - selectors works on high-level objects, and is more portable.

# select() takes 3 arguments:
# - 3 lists of objects to monitor: rlist, wlist, xlist.
#   - These are the objects to 'select' from.
#   - The lists are modified in-place to contain only the objects that have data available to read,
#     or are ready to accept data to be written.
#     - And, you can tell which list the object was in originally by looking at the list it was in
#       after the call to select().
#   - If an object in a list is ready, it is removed from the list and returned.
#   - If the list is empty, select() returns an empty list.
#   - If the list is None, select() just ignores it
