import select
# Test select.select, with timeout.
import nose

class tselect:
#		try:
#			self.chko(select.select([], [], [], 0.001), ([], [], []))
#		except select.error, e:
#			if e.args[0] != errno.EINTR:
#				self.chko(e.args[0], errno.EBADF)
	def test1_000(self):
		self.chko(select.select([], [], []), ([], [], []))
	def test1_001(self):
		self.chko(select.select([], [], []), ([], [], []))
	def test2_000(self):
		self.chko(select.select([1], [], []), ([1], [], []))
	def test3_000(self):
		self.chko(select.select([], [2], []), ([], [2], []))
	def test3_001(self):
		self.ch
