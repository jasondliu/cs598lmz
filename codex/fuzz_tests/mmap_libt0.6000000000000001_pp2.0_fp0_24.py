import mmap
+
+#Connect to the input file
+f = open('input.txt', 'r')
+
+#Memory map the input file
+m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+
+#Read the input file
+input = m.readline()
+
+#Close the input file
+m.close()
+f.close()
+
+#Split the input into a list
+input = input.split(",")
+
+#Convert the list into integers
+for i in range(len(input)):
+    input[i] = int(input[i])
+
+#Define the function that will calculate the output
+def calculate(noun, verb):
+    #Set the first two values in the input list to the noun and verb
+    input[1] = noun
+    input[2] = verb
+
+    #Loop through the input list four values at a time
+    for i in range(0, len(input), 4):
+        #If the
