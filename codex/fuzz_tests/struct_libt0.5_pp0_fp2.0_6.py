import _struct
+
+
+def test_struct_pack():
+    data = _struct.pack('>ii', 1, 2)
+    assert data == b'\x00\x00\x00\x01\x00\x00\x00\x02'
+
+
+def test_struct_unpack():
+    data = b'\x00\x00\x00\x01\x00\x00\x00\x02'
+    assert _struct.unpack('>ii', data) == (1, 2)

