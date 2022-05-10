import mmap
+
+def main(inputs, output):
+    
+    header = []
+    header.append("#version 3.7;")
+    header.append("#include \"standard.inc\"")
+    header.append("")
+    header.append("global_settings { assumed_gamma 1.0 }")
+    header.append("")
+    header.append("camera {")
+    header.append("    location    <0, 0, 0>")
+    header.append("    direction   <0, 0, 1>")
+    header.append("    right       <1.33333, 0, 0>")
+    header.append("    up          <0, 1, 0>")
+    header.append("    look_at     <0, 0, -1>")
+    header.append("}")
+    header.append("")
+    header.append("light_source {")
+    header.append("    <0, 0, 0>")
+    header.append("    color rgb <1, 1, 1>")
