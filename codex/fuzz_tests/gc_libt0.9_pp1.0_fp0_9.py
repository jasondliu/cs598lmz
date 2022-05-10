import gc, weakref
+import random, pprint
+
+# TODO - wrap interface to make it easier
+# set is a set of values, eg: [('x', 'y'), 1, (3, 4), (5, 6, 7)]
+def ignore_duplicates(set, value):
+	return False
+	# TODO
+	# value should be an immutable object
+	# return yes/no
+
+DUPLICATE_KEY = 'duplicate'
+
+def duplicate(set, value):
+	# TODO
+	return DUPLICATE_KEY
+
+def join_dicts(dicts, on=0, select=1):
+	joined = {}
+	for a_dict in dicts:
+		for k, v in a_dict.items():
+			if joined.has_key(k):
+				joined[k].append(v)
+			else:
+				joined[k] = [v]
+	return joined
+
+# TODO - this could
