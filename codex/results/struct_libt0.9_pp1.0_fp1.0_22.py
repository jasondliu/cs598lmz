import _struct
+import csv
+
+data_path = _path.join(_os.environ["DATA_PATH"], "images")
+object_path = _path.join(_os.environ["DATA_PATH"], "objects")
+
+data_file = _path.join(data_path, "data.csv")
+
+
+def imread(path):
+    image = _cv.imread(path)
+    image = _cv.cvtColor(image, _cv.COLOR_BGR2RGB)
+    return image
+
+
+def get_data():
+    encoded_data = []
+    labels = []
+    with open(image_data_file, "r") as file:
+        reader = csv.reader(file)
+        for row in reader:
+            image_path = row[0]
+            image = imread(image_path)
+            encoded_data.append(image)
+            label_path = row[1]
+            label = load_pickle(label_path)
+            labels
