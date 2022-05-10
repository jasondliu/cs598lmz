import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libopenblas.dylib')
# We can call, e.g. numpy.dot() with this.

# From https://github.com/scipy/scipy/issues/5998
# Unfortunately, the load order matters.  If we do:
import numpy
import scipy
# Then subsequent numpy.dot() calls default to numpy's BLAS and are SLOW.

# To remedy this, we use:
import scipy # Make scipy try and link against OpenBlas
import numpy

# Now we can use numpy.dot(), because it's linked against scipy's.
</code>
I understand the OS X system we built uWSGI with may have been configured with different options, and though our code base is the same, it's necessary for us to use different BLAS libraries depending on where we're running.
I need to configure uWSGI to not use the Apple BLAS libraries, but I want to do this as early in the process as possible/reasonable.  Is there somewhere to set this environment variable that isn't
