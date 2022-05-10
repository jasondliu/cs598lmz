import _struct
import _keccak

# Public API
# ==========
# exported functions (note that this is a Python 2/3 compatible wrapper!)
#
# bytes     keccak(int digest_bits, bytes message)
# bytes     keccakf(bytes state)
# bytes     keccak1600(bytes message)
# bytes     sha3_224(bytes message)
# bytes     sha3_256(bytes message)
# bytes     sha3_384(bytes message)
# bytes     sha3_512(bytes message)

# implementation functions (c-api not planned)
#
# bytes     pad10star1(bytes message, int m, int n)
# bytes     bytestring_to_state(bytes message)
# bytes     state_to_bytestring(bytes state)


# Keccak sponge function
def keccak(digest_bits, message):
    # default parameter
    if digest_bits == 0:
        digest_bits = 512

    # check parameter
    if not (0 <= digest_bits <= 1600) or digest_bits % 8
