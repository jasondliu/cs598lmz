import _struct
+import array
+import random
+
+
+def read_mnist(images_path, labels_path):
+    with open(labels_path, 'rb') as labels_file:
+        magic, n = _struct.unpack('>II', labels_file.read(8))
+        labels = array.array('B', labels_file.read())
+    with open(images_path, 'rb') as images_file:
+        magic, num, rows, cols = _struct.unpack('>IIII', images_file.read(16))
+        images = array.array('B', images_file.read())
+    return images, labels, rows, cols
+
+
+def display(images, labels, rows, cols):
+    width, height = rows, cols
+    n = len(images)
+    plt.figure()
+    plt.gray()
+    for i in range(n):
+        plt.subplot(10, 10, i + 1)
+        plt.title(lab
