import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
#两个字符串都被删除了，说明弱引用callback执行了
# class Graph(object):
#     def __init__(self,name):
#         self.name=name
#         self.nodes=[]
#         self.edges=[]
#     def add_node(self,node):
#         if node in self.nodes:
#             raise ValueError('Duplicate node')
#         else:
#             self.nodes.append(node)
#     def add_edge(self,edge):
#         for e in self.edges:
#             if e[0]==edge[0] and e[1]==edge[1]:
#                 raise ValueError('Duplicate edge')
#             self.edges.append(edge)
#     def del_node(self,node):
#         try:
#             self.nodes
