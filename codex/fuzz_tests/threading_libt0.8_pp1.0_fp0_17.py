import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return

		curr_node = self.head
		while curr_node.next:
			curr_node = curr_node.next
		curr_node.next = new_node

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data, end = ' ')
			cur_
