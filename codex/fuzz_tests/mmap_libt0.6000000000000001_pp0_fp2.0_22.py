import mmap
+import re
+import sys
+
+# Open a file
+fd = os.open( "foo.txt", os.O_RDWR )
+
+# Memory-map the file, size 0 means whole file
+mapped_file = mmap.mmap( fd, 0 )
+
+# Close the file
+os.close( fd )
+
+# Read content via standard file methods
+print mapped_file.readline()
+
+# Update content using slice notation;
+# note that new content must have same size
+# as original content
+mapped_file[6:11] = " world"
+mapped_file.close()
+
+# Re-open the file
+fd = os.open( "foo.txt", os.O_RDWR )
+
+# Memory-map the file, size 0 means whole file
+mapped_file = mmap.mmap( fd, 0 )
+
+# Close the file
+os.close( fd )
+
+# Verify that changes were made
+print mapped
