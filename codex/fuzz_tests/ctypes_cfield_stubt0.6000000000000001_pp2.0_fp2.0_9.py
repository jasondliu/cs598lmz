import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class TypeChecker(ast.NodeVisitor):
    def __init__(self, vars, types):
        self.vars = vars
        self.types = types

    def visit_Name(self, node):
        if node.id not in self.vars:
            raise ValueError(node.id)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        if type(node.op) is ast.Add:
            if self.types[node.left.id] is not self.types[node.right.id]:
                raise ValueError(node.left.id, node.right.id)

    def visit_Assign(self, node):
        self.visit(node.value)
        self.types[node.targets[0].id] = self.types[node.value.id]

class VariableChecker(ast.NodeVisitor):
    def __init__(self, vars, types):
        self.vars = vars
