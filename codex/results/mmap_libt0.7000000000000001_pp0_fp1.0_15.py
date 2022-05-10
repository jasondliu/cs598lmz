import mmap
+
+
+def load_memory_map(filename, dtype, shape=(), mode='c'):
+    '''
+    Load a numpy array from a binary file on disk
+    using a memory map.
+    Arguments
+    ---------
+    filename : str
+        The path to the binary file on disk.
+    dtype : str or numpy dtype
+        The array's data type.
+    shape : tuple
+        The shape of the array.
+    mode : str
+        The memory map's mode.
+    Returns
+    -------
+    A numpy array.
+    '''
+    dtype = np.dtype(dtype)
+    shape = tuple(shape)
+
+    with open(filename, 'r+b') as f:
+        size = f.seek(0, 2)
+        size = f.tell()
+
+        if size == np.prod(shape, dtype=np.int64) * dtype.itemsize:
+            memmap = np.memmap
