import _struct
+from PIL import Image
+from io import BytesIO
+from scipy import stats
+#from operator import itemgetter
+from itertools import groupby
+from scipy.ndimage.measurements import center_of_mass
+from scipy import cluster
+import random
+
+
+
+#from PIL import Image
+def centralise(data):
+  coords = np.array(np.where(data == 1))
+  com = center_of_mass(data)
+  data = np.roll(data, -(com[0] - coords[0]), axis=0)
+  data = np.roll(data, -(com[1] - coords[1]), axis=1)
+  return data
+
+def min_max( data, min=0.0, max=1.0):
+  data -= data.min()
+  data *= (float(max - min) / data.max())
+  data += min
+  return np.array(data, dtype='uint8
