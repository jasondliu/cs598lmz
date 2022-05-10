from types import FunctionType
list(FunctionType(3, None, (), ('x', 'y', 'z'), (None, None, None, False, False), None))
"""
        suite = ast.Suite([ast.ExpressionStatement(exp)])
        node = ast.Module(suite)
        self.assertEqual(self.eval(node), [1, 2, 3])

        exp = """\
from operator import neg
list(map(neg, [-1, -2, -3]))
"""
        suite = ast.Suite([ast.ExpressionStatement(exp)])
        node = ast.Module(suite)
        self.assertEqual(self.eval(node), [1, 2, 3])

        exp = """\
from operator import truediv
list(map(truediv, [1, 2, 3], [1, 1, 1]))
"""
        suite = ast.Suite([ast.ExpressionStatement(exp)])
        node = ast.Module(suite)
        self.assertEqual(self.eval(node), [1, 2, 3])

    def test_issue156
