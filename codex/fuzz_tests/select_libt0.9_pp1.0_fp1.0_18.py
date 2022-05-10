import selectivesearch
+
+class VocabTree:
+    def __init__(self, n_clusters, kmeans_args):
+        self.n_clusters = n_clusters
+        
+        self.vocab_tree_index = faiss.IndexFlatL2(self.n_clusters)
+
+        self.kmeans_args = kmeans_args
+
+        self.tier = 0
+
+        self.leaf_size = 0
+
+    def set_input(self):
+        pass
+    
+    def learn_vocab(self, features):
+        
+        if self.tier == 0:
+            self.vocab_tree_index = faiss.index_cpu_to_gpu(self.vocab_tree_index, 0)
+
+        self.n_clusters *= 2
+        
+        self._cluster_features(features)
+        
+        # self.vocab_tree_index = faiss.IndexFlatL2(self.n_cl
