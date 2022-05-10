import types
types.new_class("Node", (object))

class Graph :
	def __init__(self, arg_nodes) :
		if arg_nodes:
			self.gui = Node(arg_nodes)

	def add_node(self, node = Node("0")) :
		if self.gui:
			node.next = self.gui
			self.gui = node
		else:
			self.gui = node

	def traverse(self, func = print) :
		node = self.gui
		while node:
			func(node.value)
			node = node.next

if __name__ == "__main__":
	g = Graph("a")
	g.add_node("b")
	g.add_node("c")

	g.traverse(lambda x : print("Reached: " + x))
