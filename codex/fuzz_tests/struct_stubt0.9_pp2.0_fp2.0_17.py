from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<7HB2I'
s.size = 31
import base64

def to_bin(s):
  bin = ''
  for i in xrange(0, len(s)):
    bin += '{0:08b}'.format(ord(s[i]))
  return bin

def to_hex(s):
  return ''.join(map(lambda x:"%02x" % ord(x), s))

def encode_bin(s):
  bin = to_bin(s)
  return '0' * (len(s) * 8 - len(bin)) + bin # left pad with 0

def decode_bin(bin):
  s = ''
  for i in xrange(len(bin) / 8):
    s += chr(int(bin[i * 8: i * 8 + 8], 2))
  return s

def bin_xor(a, b):
  if len(a) != len(b):
    return ''
  res = ''
  for i in xrange(len(a)):
