import lzma
lzma.__file__

# Check if lzma is in the same directory as the file being executed
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lzma"))

# Add the lzma module to the Python path
#try:
#    import lzma
#except ImportError:
#    sys.stderr.write("Error: Cannot find the lzma library and/or module.")
#    sys.stderr.write("Make sure that it is in the same directory as this")
#    sys.stderr.write("program or consult the documentation at")
#    sys.stderr.write("http://docs.python.org/3/install/")
#    sys.stderr.write("for help installing third-party modules.")
#    sys.exit(1)

#==============================================================================

# Check if the lzma module is from the Python 3.3+ standard library
