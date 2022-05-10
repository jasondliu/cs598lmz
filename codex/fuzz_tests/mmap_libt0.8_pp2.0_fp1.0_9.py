import mmap
+import time
+
+
+emu = LxEmu()
+
+
+def copy_to_usr(emu, usr_offset, src, src_offset, size):
+    assert type(src) == bytes
+    assert type(usr_offset) == int
+    assert type(src_offset) == int
+    assert type(size) == int
+    emu.mem_write(usr_offset, src[src_offset:src_offset+size])
+
+
+def copy_from_usr(emu, usr_offset, dst, dst_offset, size):
+    assert type(dst) == bytes
+    assert type(usr_offset) == int
+    assert type(dst_offset) == int
+    assert type(size) == int
+    dst[dst_offset:dst_offset+size] = emu.mem_read(usr_offset, size)
+    return dst
+
+
+def leak_fd(fd):
+    mem = mmap.mmap(-1, 0
