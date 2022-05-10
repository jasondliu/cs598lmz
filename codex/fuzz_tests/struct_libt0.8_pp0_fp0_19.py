import _struct
+
+# 定义训练数据
+train_images_idx3_ubyte_file = 'train-images.idx3-ubyte'
+# 训练数据label
+train_labels_idx1_ubyte_file = 'train-labels.idx1-ubyte'
+
+# 定义测试数据
+test_images_idx3_ubyte_file = 't10k-images.idx3-ubyte'
+# 测试数据label
+test_labels_idx1_ubyte_file = 't10k-labels.idx1-ubyte'
+
+# 定义解析数据函数
+def decode_idx3_ubyte(idx3_ubyte_file):
+    """
+    解析id
