import mmap
+import time
+
+#
+# This is not a complete example, it only shows how to read from the
+# shared memory.
+#
+
+#
+# This is the size of the shared memory block
+#
+size = 1024
+
+#
+# This is the "file" name of the shared memory block.
+# The kernel will use this name to create the shared memory block.
+#
+shm_name = "/my_shm"
+
+#
+# This is the shared memory object.
+#
+shm = None
+
+#
+# This is the memory map to the shared memory block.
+#
+shm_map = None
+
+#
+# Open the shared memory block.
+#
+shm = posix_ipc.SharedMemory(shm_name, flags=posix_ipc.O_CREX, mode=0o777, size=size)
+
+#
+# Create the memory map to the shared memory block.
+#
+shm_map
