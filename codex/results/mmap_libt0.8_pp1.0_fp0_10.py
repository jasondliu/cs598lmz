import mmap
+import collections
+
+# First, mmap a file so that we can upload it to SWAP 
+# And get the address of it
+#
+#
+
+with open("audio.raw", "r+b") as f:
+    m = mmap.mmap(f.fileno(), 0)
+    print(m.read(16))
+    print(hex(m.tell()))
+    print(hex(id(m)))
+
+# Second, we need to upload the file to SWAP
+#
+#
+
+# Third, we need to create a DMA descriptor for the SWAP
+#
+#
+
+# Fourth, we need to configure the DMA
+#
+#
+
+# Fifth, we need to start the DMA
+#
+#
+
+# Sixth, we need to start the audio DMAC
+#
+#
+
+# Seventh, we need to set the address of the audio data to the one
+# that we got from SWAP
+#
+#

