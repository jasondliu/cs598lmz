import weakref
+
+from . import version
+
+
+class ImageFilter(object):
+    """
+    ImageFilter is a base class for all image filters.
+    """
+    name = "Base"
+    version = version.__version__
+
+    def __init__(self):
+        self.input_image = None
+        self.output_image = None
+        
+    def setInputImage(self, image):
+        """
+        Set the input image (a numpy array)
+
+        Parameters
+        ----------
+        image : ndarray
+            a numpy ndarray image
+
+        """
+        self.input_image = image
+        
+    def getOutputImage(self):
+        """
+        Get the output image as a numpy ndarray
+        """
+        return self.output_image
+    
+    def update(self):
+        """
+        Run the filter on the input image
+        """
+        raise NotImplementedError("This is a
