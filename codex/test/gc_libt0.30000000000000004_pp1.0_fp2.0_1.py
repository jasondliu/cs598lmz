import gc, weakref

#
# The following code is used to keep a cache of previously created objects.
# This can be used to ensure that two objects with the same ID will in fact
# be the same object.
#

