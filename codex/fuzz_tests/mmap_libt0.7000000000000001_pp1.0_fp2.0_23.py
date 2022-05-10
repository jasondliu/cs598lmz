import mmap
+
+
+def file_size(filename):
+    """Return the size of a file in bytes"""
+    return os.stat(filename).st_size
+
+
+def generate_file(filename, size):
+    """Generate a file of given size with random data"""
+    with open(filename, 'wb') as f:
+        f.write(os.urandom(size))
+
+
+def generate_files(num_files, size):
+    """Generate a number of files of given size with random data"""
+    for i in range(1, num_files + 1):
+        filename = f"test_file_{i}"
+        generate_file(filename, size)
+
+
+@pytest.fixture(scope='function')
+def generate_test_files():
+    """Generate test files"""
+    generate_files(10, 100000)
+    yield
+    for file in os.listdir(os.getcwd()):
+        if file.startswith('test_file_'
