import mmap, re
+
+# Change these values to define the area of the map to process
+# (in decimal degrees)
+lat1 = 42.669746
+lat2 = 49.001312
+lon1 = 5.967041
+lon2 = 15.021484
+
+# Footprint of the map
+footprint = [[lat1,lon1],[lat1,lon2],[lat2,lon2],[lat2,lon1],[lat1,lon1]]
+
+# Open OSM map file
+f = open('switzerland-latest.osm', 'rb')
+s1 = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+# Read the entire file at once
+s = s1.read()
+
+# Close map file
+s1.close()
+
+# Preprocess the OSM data to speed up the following search
+# (replace all HTML-like tags by spaces)
+s = re.sub(r'<[^<]+?>', ' ', s)
