import codecs
# Test codecs.register_error
# Run this test with "python -Wdefault codecs_registration.py"
# to make sure that the warning is triggered.

import test.test_support, codecs, sys
import warnings

def test_main():
    warnings.filterwarnings("error", "", DeprecationWarning, "test_codecs")
    try:
        codecs.register_error("test.test_codecs", None)
    except DeprecationWarning:
        pass
    else:
        raise TestFailed("register_error() should have raised a DeprecationWarning")

if __name__ == "__main__":
    test_main()
