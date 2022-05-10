import mmap
+import random
+import sys
+import copy
+import os
+
+
+
+def main():
+    """
+    This is the main entry point for the program
+    """
+    print("Hello World!")
+    
+    inputs = sys.argv[1:]
+    #print(inputs)
+    #print(len(inputs))
+    
+    print(str(inputs[0]) + " " + str(inputs[1]) + " " + str(inputs[2]))
+    
+    generate(int(inputs[0]),int(inputs[1]),int(inputs[2]))
+
+
+def generate(width, height, density):
+    width = int(width)
+    height = int(height)
+    density = int(density)
+    
+    maze = [[0 for x in range(width)] for y in range(height)]
+    #maze.fill(0)
+    #print("Initial maze: ")
+    print_maze(
