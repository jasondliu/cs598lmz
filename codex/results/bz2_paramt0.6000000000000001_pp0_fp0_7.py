from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#  bz2.BZ2Compressor().compress(data) + bz2.BZ2Compressor().flush()
#  bz2.BZ2Decompressor().decompress(data)


#  def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):
#      """Password based key derivation function 2 (PKCS #5 v2.0)
#
#      This Python implementations based on the hmac module about as fast
#      as OpenSSL's PKCS5_PBKDF2_HMAC for short passwords and much faster
#      for long passwords.
#      """
#      if not isinstance(hash_name, bytes):
#          hash_name = hash_name.encode('ascii')
#      if not isinstance(password, bytes):
#          password = password.encode('utf-8')
#      if not isinstance(salt, bytes):
#          salt = salt.encode('ascii')
#
#      # Fast inline HM
