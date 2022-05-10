import mmap
+from contextlib import contextmanager
+
+import numpy as np
+from PIL import Image
+from torchvision.transforms import ToTensor, ToPILImage, Normalize
+
+
+@contextmanager
+def mmap_file(filename, *args, **kwargs):
+    f = open(filename, *args, **kwargs)
+    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+    try:
+        yield mm
+    finally:
+        mm.close()
+
+
+def load_jpeg_to_tensor(filename):
+    with mmap_file(filename, 'rb') as f:
+        img = np.frombuffer(f.read(), dtype=np.uint8)
+
+    img = img.reshape(1024, 1024, 3)
+    img = Image.fromarray(img)
+
+    return ToTensor()(img)
+
+
+if __name__ == '__main__':
+
