import _struct
+
+
+class PCA_Calculator:
+
+    def __init__(self, data, labels):
+        self.data = data
+        self.labels = labels
+
+    def mean(self):
+        """
+        :return: mean of the data
+        """
+        return np.mean(self.data, axis=0)
+
+    def center_data(self):
+        """
+        :return: centered data
+        """
+        return self.data - self.mean()
+
+    def covariance_matrix(self):
+        """
+        :return: covariance matrix
+        """
+        return np.cov(self.data.T)
+
+    def eig(self):
+        """
+        :return: eigenvalues and eigenvectors of the covariance matrix
+        """
+        return np.linalg.eig(self.covariance_matrix())
+
+    def order(self):
+        """
+       
