import codecs
# Test codecs.register_error

# This test is meant to be run from the command line.
# It is not run automatically by the test suite.

# The test is run with the following command:
#   python test_register_error.py

# The test prints a message if it fails.
# The test prints nothing if it succeeds.

# The test fails if the codecs module raises an exception.

# The test is supposed to be run with the following environment variables
# set to the values shown:
#
# PYTHONPATH=.
# PYTHONSTARTUP=test_register_error.py
#
# The PYTHONSTARTUP environment variable causes the Python interpreter
# to run the script test_register_error.py before reading the command line.
# The script test_register_error.py registers a codec error handler
# for the "test_register_error" codec.
#
# The test is run with the following command:
#
# python -c 'import codecs; print codecs.getencoder("test_register_error")("abc")'
#
# The test succeeds if
