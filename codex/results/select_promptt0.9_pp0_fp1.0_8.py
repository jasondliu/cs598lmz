import select
# Test select.select
import socket

def test_select():
	socketlist = []
	socketlist.append(socket.socket())
	socketlist.append(socket.socket())
	print(select.select(socketlist,[],[],10))

class Test(unittest.TestCase):
	def test(self):
		test_select()

def main():
	unittest.main()

if __name__ == '__main__':
	main()
