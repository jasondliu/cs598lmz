import select
+import sys
+
+# select.select(rlist, wlist, xlist[, timeout])
+# rlist: 待读文件描述符列表
+# wlist: 待写文件描述符列表
+# xlist: 异常条件文件描述符列表
+# timeout: 超时时间
+# 返回值：三个列表，分别为可读、可写、异常
+# 如果没有可操作的文件描述符并且没有超时，select会阻塞
+
+inputs = [sys.stdin]
+while True:
+    rs, ws, es = select.select(inputs,
