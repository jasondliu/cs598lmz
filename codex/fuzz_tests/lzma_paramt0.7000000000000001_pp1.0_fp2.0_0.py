from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
I get the error:
<code>Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/paramiko/transport.py", line 1677, in run
    self.kex_engine.parse_next(ptype, m)
  File "/usr/local/lib/python3.6/dist-packages/paramiko/kex_ecdh_nist.py", line 81, in parse_next
    return KexNist.parse_next(self, ptype, m)
  File "/usr/local/lib/python3.6/dist-packages/paramiko/kex_nist.py", line 73, in parse_next
    return self._parse_next(ptype, m)
  File "/usr/local/lib/python3.6/dist-packages/paramiko/kex_nist.py", line 79, in _parse_next
    return Kex._parse_next(self, ptype, m)
  File "/usr/local/lib/
