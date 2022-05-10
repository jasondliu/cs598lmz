import types
types.NoneType.__str__ = lambda self: ""

#import sys
#sys.path.append(base+'/python')

## Use the PyXB Python module to generate/connect 
##   to PyXML Bindings (i.e. the Python bindings 
##   module that maps XML schema to Python objects)

## used to pep8 check the generated code
# The pep8 module
# http://pypi.python.org/pypi/pep8
# Try "easy_install pep8"

# The autopep8 tool
# https://pypi.python.org/pypi/autopep8
# Try "easy_install autopep8" or view the documentation at:
# https://github.com/hhatto/autopep8

import autopep8

print "IMPORTING PYXB BINDINGS FOR MARS XML SCHEMA"

try:
    import mars_bindings_generated_compiled as mars

except Exception:
    print "WARNING: failed to import compiled bindings; will try to generate from scratch"
   
