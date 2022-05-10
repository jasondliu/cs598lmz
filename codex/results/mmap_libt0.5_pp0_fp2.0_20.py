import mmap
+import os
+
+def main():
+    # Open the file
+    fd = os.open('/tmp/mmap_example.bin', os.O_RDWR | os.O_CREAT)
+
+    # Zero out the file to illustrate the point of copy-on-write
+    os.write(fd, '\x00' * mmap.PAGESIZE)
+
+    # Create the mmap instace with the following params:
+    # fd: File descriptor which backs the mapping or -1 for anonymous mapping
+    # length: Must in multiples of PAGESIZE (usually 4 KB)
+    # flags: MAP_SHARED means other processes can share this mmap
+    # prot: PROT_WRITE means this process can write to this mmap
+    m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)
+
+    # Write to the mmap
+    m.write('Hello')
+
+    # Close the file descriptor
