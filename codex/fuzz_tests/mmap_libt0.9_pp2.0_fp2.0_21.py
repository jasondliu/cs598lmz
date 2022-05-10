import mmap
+import struct
+
+
+def get_image_header():
+    """Read image header"""
+    image_header = {}
+    with open('YOUR_IMAGE_FILE', 'rb') as file:
+        image = mmap.mmap(file.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
+        image_header['Byte Order'] = image[1:3].hex()
+        image_header['Magic'] = image[5:6].hex()
+        magic = int(image_header['Magic'], 16)
+        if magic == 2:
+            image_header['Magic'] = "INTEL_MAGIC"
+        elif magic == 3:
+            image_header['Magic'] = "SPARC_MAGIC"
+        image_header['CPU Type'] = str(int(image[0:1].hex(), 16))
+        image_header['CPU Type'] = struct.pack('<I', int(image_header['CPU Type']))
+        if image_header['CPU Type
