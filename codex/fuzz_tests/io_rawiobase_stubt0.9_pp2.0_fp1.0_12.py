import io
class File(io.RawIOBase): -->
+	def readinto(self, b)：
+		s = self.read(len(b))
+		n = len(s)
+		b[:n] = s
+		return n
+- [1, 2, 3] * 2
+- count([1, 2, 3], 2)
+剑指offer上的一道题：在一个字符串中找到第一个只出现一次的字符。
+是否可以使用桶排序-》hashmap-》分配特定空间，第一次给1，第二次给0，一定要考虑溢出问题。

