import weakref
# Test weakref.ref when finalizer is autoref on a custom object.

# This tests the type structure changes made by
# commit 9de4078c102b495e27db931d7f60b0defe83b8f0
# If the autoref leak fix commit broke this,
# the test will segfault with error message:
#     Fatal Python error: deallocating None
# or
#     Fatal Python error: deallocating <built-in function __del__>
#
# Note that this error can happen by executing the equivalent of:
#     refs = weakref.allrefs()
#     del refs
#     gc.collect()
#
# So, this is testing that the objects are properly registered
# and cleaned up when they should be.


class ExpensiveList(object):

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def __delitem__(self, item):
        self.items.remove(item)

    def __len__(self):

