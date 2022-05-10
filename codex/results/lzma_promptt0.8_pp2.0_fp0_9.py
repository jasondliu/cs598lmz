import lzma
# Test LZMADecompressor output
# >>> LZMADecompressor().decompress(data)


# TODO: as a general principle, have a Unit Test that writes a test file, then tests it can read it.
#
#
#
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# TODO: Adjust the wait time for the header content
# TODO: Adjust the protocol for header / trailer responses
# TODO: If the header has reached its pre-determined size,
#       Start sending the contents of the file
# TODO: Monitor the time it takes for a response
# TODO: Implement acknowledgements
# TODO: If there is no response to the header, do it multiple times


# The file name is in the first line of the header
# We can call the header the "Header packet"

# ********************************************************************************
# ** Main class for sending the file
# ********************************************************************************

class Send:
    # We may need to instantiate this class multiple times
    #   For example, if we want to send a file more than once
   
