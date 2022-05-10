import mmap
+import numpy as np
+import array
+
+directory = '/home/jiaqi/software/faiss/data/'
+
+# 需要匹配的目标向量: 存储的是id和query的组合，id和query的组合通过#号分割
+target = np.random.random((2, 64)).astype('float32')
+target[0, :] += 100
+target_file = directory + 'target'
+target.tofile(target_file)
+
+# 需要被匹配的影响因子：存储的是feature_index和feature_value交叉连续存储
+feat = np.random.random((4, 32)) * 100
+feat_file = directory + 'feat'
+feat.tofile(feat_file)
+
+
+#
