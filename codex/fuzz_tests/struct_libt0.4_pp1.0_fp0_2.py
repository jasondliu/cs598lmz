import _struct
+
+import numpy as np
+
+
+def read_idx(filename):
+    with open(filename, 'rb') as f:
+        zero, data_type, dims = _struct.unpack('>HBB', f.read(4))
+        shape = tuple(dims[i] * (dtype >> (i * 8)) & 255
+                      for i in range(len(dims))[::-1])
+        return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)
+
+
+def read_mnist(dataset="training", path="."):
+    """
+    Python function for importing the MNIST data set.
+    """
+
+    if dataset is "training":
+        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
+        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
+    elif dataset is "
