import signal
# Test signal.setitimer()
import test.test_signal as test_signal

# tests using urllib
import test.test_urllib
test.test_urllib.test_main()

# tests using urlparse
import test.test_urlparse
test.test_urlparse.test_main()

# tests using gzip
import test.test_gzip
test.test_gzip.test_main()

# tests from test_pep247
import test.test_pep247 # docstring

# tests for weakref
import test.test_weakref
test.test_weakref.test_main()

# tests for linecache
import test.test_linecache
test.test_linecache.test_main()

# tests for struct
import test.test_struct
test.test_struct.test_main()

# tests for doctest
import test.test_doctest
test.test_doctest.test_main()

# tests for pickle
import test.test_pickle
test.test_pickle.test_main()


