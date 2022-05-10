import select
+
+def get_IP_table(IP_file):
+    IP_table = []
+    file = open(IP_file)
+    for i in range(256):
+        IP_table.append([])
+        line = file.readline().strip('\n')
+        IP_table[i] = line.split(',')
+    return IP_table
+
+def get_IP_table_port(IP_table,port_file):
+    port_table = []
+    file = open(port_file)
+    for i in range(256):
+        port_table.append([])
+        line = file.readline().strip('\n')
+        if line != '':
+            port_table[i] = line.split(',')
+        else:
+            port_table[i] = IP_table[i]
+    return port_table
+
+
+def create_IP_port_table(path):
+    port_file = open(path+'port_table.txt','w
