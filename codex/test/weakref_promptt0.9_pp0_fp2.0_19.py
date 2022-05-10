import weakref
# Test weakref.ref
if weakref.ref != weakref.ReferenceType:
    # Jython
    import org.python.core.class_
    org.python.core.class_.forName('weakref.ref')._rename('ReferenceType')
