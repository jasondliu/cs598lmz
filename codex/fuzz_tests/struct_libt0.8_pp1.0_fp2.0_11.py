import _struct
+
+# inflate the cleartext
+b = bz2.decompress(bz2.BZ2Decompressor().decompress(ciphertext))
+
+# get the header
+header = b[:6]
+flags = _struct.unpack("=BBBBB", header)
+
+(ctype, mtype, mlen, mlen_salt, mlen_iv) = flags
+
+mlen_seq = 8
+mlen_tag = 16
+mlen_aad = 0
+
+# decrypt
+plaintext = fernet.Fernet(key).decrypt(b[6:])
+
+print(plaintext)
+

