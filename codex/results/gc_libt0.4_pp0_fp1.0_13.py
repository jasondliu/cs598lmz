import gc, weakref

from . import utils
from . import _py2to3

# TODO:
#  * Use weakrefs to avoid circular references
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses)
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses) with a given attribute
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses) with a given attribute with a given value
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses) with a given attribute with a given value
#    and a given parent
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses) with a given attribute with a given value
#    and a given parent
#  * Add a way to get the list of all objects of a given class
#    (and possibly subclasses) with a given attribute with a given value
#    and a given parent and a
