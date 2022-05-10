import _struct
+
+def reverse_hex(s):
+  return _struct.pack("<I", _struct.unpack("<I", s)[0])
+
+def get_rand(s):
+  return ntlm.compute_lmhash(utils.string.smart_str(s))[:8]
+
+def e(s):
+  return base64.b64encode(s)
+
+def d(s):
+  return base64.b64decode(s)
+
+def eh(s):
+  return e(reverse_hex(s)).strip("= ")
+
+def deh(s):
+  return reverse_hex(d(s.replace(" ", "=")))
+
+s = input("s: ")
+p = get_rand(s)
+c = pyDes.des(reverse_hex(p))
+t = input("t: ")
+print("Password:", eh(e(reverse_hex(p + c._pad(t)))))

