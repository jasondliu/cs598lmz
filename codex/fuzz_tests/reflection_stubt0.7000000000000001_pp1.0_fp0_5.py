fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi

import ast
import io

class MyVisitor(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.FunctionDef):
            self.visit_FunctionDef(node)
        else:
            ast.NodeVisitor.visit(self, node)

    def visit_FunctionDef(self, node):
        node.body[0].value.args[0].id = 'y'
        ast.NodeVisitor.generic_visit(self, node)

myvisitor = MyVisitor()
myvisitor.visit(ast.parse(inspect.getsource(fn)))
exec(compile(ast.parse(inspect.getsource(fn)), '', 'exec'), globals(), locals())
fn()
</code>

