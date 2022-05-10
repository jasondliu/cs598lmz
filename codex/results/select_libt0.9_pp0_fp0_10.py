import select
+import time
+import struct
+
+
+def findECU(bluetoothSocket, Address=0x0, Id=0x0, Type=None, returnIndex=False, verbose=False, ECUs=None):
+    if not ECUs == None:
+        for k, ECU in enumerate(ECUs):
+            if (Address == 0 or Address == ECU[0]) and (Id == 0 or Id == ECU[1]) and (Type == None or Type == ECU[2]):
+                if returnIndex:
+                    return k, ECU
+                else:
+                    return ECU
+        print "No ECU Found"
+        return None
+    else:
+        ECUs = []
+        for address in xrange(0x10, 0xF7, 0x10):
+            for id in xrange(0x00, 0xF0, 0x10):
+                if address == 0xF0:
+                    if id == 0x60:
+                        id = 0xA0
+                    else:
