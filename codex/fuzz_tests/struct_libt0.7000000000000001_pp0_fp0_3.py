import _struct
+
+
+class BERInteger(object):
+    """
+    BER Integer
+
+    A BER integer is a signed integer encoded as a sequence of octets,
+    the value of which is determined by the most significant bit of the
+    first octet. The first bit of the first octet is the most significant
+    bit.
+    """
+    def __init__(self, value):
+        if isinstance(value, int):
+            self.value = value
+        else:
+            raise TypeError("value must be integer")
+
+    @property
+    def encoded(self):
+        value = self.value
+        bytes_ = []
+        while value != 0:
+            bytes_.append(value & 0xff)
+            value = value >> 8
+        if bytes_[0] & 0x80:
+            bytes_[0] = bytes_[0] & 0x7f
+            bytes_.insert(0, 0)
+        return bytes(bytes_)
+
+    @classmethod
