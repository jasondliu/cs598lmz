import _struct

import BitGet
import BitDistance

MAX_CODE_LENGTH = 32

# Number of bits used to determine the length of a code
CODE_LENGTH_BITS = 4

# Number of bits used to store the length of a code - there are 2^CODE_LENGTH_BITS
# codes of length greater than or equal to CODE_LENGTH_BITS
SHORT_CODE_LENGTHS = (1 << CODE_LENGTH_BITS) - 1

# First byte after the encoding data
ENCODED_DATA_START = 1 + SHORT_CODE_LENGTHS

def getCumulative(lengths, maxlen):
    """
    Get the cumulative code length counts.
    @c len is the number of symbols with codes len bits long.
    @c maxlen is the number of bits of longest code.
    @c nextcode contains the first code for each length,
    i.e. the first code of length 1 is in @c nextcode[1], the first
    code of length 2 is in @c nextcode[2].
    @
