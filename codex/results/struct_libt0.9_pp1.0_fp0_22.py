import _struct
+
+MAX_PATH = 260
+FORMAT = 'LLLLLL'
+SIZE = struct.calcsize(FORMAT)
+
+
+class Memory:
+    def __init__(self, pid):
+        self.pid = pid
+        self.process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, self.pid)
+
+    def read(self, address):
+        buffer = c_ulonglong()
+        bytes_read = c_ulonglong()
+        ReadProcessMemory(self.process_handle, address, byref(buffer), SIZE, byref(bytes_read))
+        return buffer.value
+
+    def write(self, address, value):
+        buffer = c_ulonglong(value)
+        bytes_written = c_ulonglong()
+        WriteProcessMemory(self.process_handle, address, byref(buffer), SIZE, byref(bytes_written))
+        return bytes_written.value
+
+
+class UnicodeString(Memory):
+   
