import select, socket, sys
+
+
+class Threader:
+	def __init__(self, num=1):
+		self.threadCount = num
+		self.works = []
+		self.threads = []
+		self.initThreads(num)
+
+	def initThreads(self, num):
+		for x in range(num):
+			t = threading.Thread(group=None, target=self.work, name=None, args=(x,))
+			self.threads.append(t)
+			t.start()
+
+	def work(self, num):
+		while True:
+			if len(self.works) > 0:
+				work = self.works.pop()
+				work.init()
+				work.do()
+				work.close()
+
+	def add(self, work):
+		self.works.append(work)
+
+

