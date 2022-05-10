import weakref
import gzip, zipfile, re
import os, sys, time

from . import dsz, os_version

# Monkey patch weakref module with support for instance methods
# and properties from PyWeakref_NewProxy.
# See also http://rosettacode.org/wiki/Weak_references
# and http://www.ferg.org/projects/python_class_decorator.html
if weakref.ReferenceType == weakref.ProxyType:
    raise WeakerReferenceError("You already have the patched version of weakref")

def Weaker(klass, *weakref_args, **weakref_kwargs):
    """
        Weaker(klass, ...
            Return a proxy for the given class which converts all instance
            methods and all instance attributes (i.e. properties) into
            weak references.
            
            This is useful when, for example, wrapping around a class which
            does not behave itself regarding garbage collection.
            
            The instance methods, instance attributes, and class attributes
            of the resulting class are determined by introspection.
    """
    
