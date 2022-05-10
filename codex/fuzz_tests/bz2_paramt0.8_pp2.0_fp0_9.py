from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

# The following is a hack for when we have both OpenSSL and pycrypto installed.
# The import of decryption.py will succeed, but only because it provides a dummy
# implementation that has a lot of its functions missing.  The actual import of
# crypto.py will then fail, because pycrypto doesn't know about the algorithms
# used by OpenSSL.  This is even worse than the normal situation where we have
# a missing library.  We therefore explicitly test for this situation and
# raise an ImportError so that the module doesn't get imported.
try:
    # This will only succeed if pycrypto is installed.
    import Crypto.PublicKey.RSA
except ImportError:
    # That's fine, we don't care if it's not installed.
    pass
else:
    # This will only succeed if OpenSSL is installed.
    try:
        from M2Crypto import RSA
    except ImportError:
        # That's fine, we don't care if it's not installed.
        pass
    else:
        # It's not fine if both are
