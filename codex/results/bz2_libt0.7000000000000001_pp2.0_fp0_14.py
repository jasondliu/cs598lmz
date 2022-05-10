import bz2
bz2.decompress(encrypted)

#cryptopals challenge 5
def repeating_key_xor(in_bytes, key):
    key_len = len(key)
    out_bytes = b""
    for n in range(0, len(in_bytes)):
        out_bytes += bytes([key[n%key_len] ^ in_bytes[n]])

    return out_bytes

input = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

repeating_key_xor(input, key)

#cryptopals challenge 6
def hamming_dist(a, b):
    assert len(a) == len(b)
    sum_res = 0
    for m, n in zip(a, b):
        if m != n:
            sum_res += bin(m ^ n).count('1')
    return sum_res

hamming_dist(b"this is a test", b"wokka wokka!!!")

#
