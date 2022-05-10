import types
types.FunctionType = types.LambdaType

class Test_Parsing(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse("1"), 1)
        self.assertEqual(parse("(1)"), 1)
        self.assertEqual(parse("(+ 1 2)"), 3)
        self.assertEqual(parse("((lambda (x) x) 1)"), 1)

    def test_nested(self):
        self.assertEqual(parse("((lambda (x) ((lambda (x) x) x)) 1)"), 1)
        self.assertEqual(parse("((lambda (x) ((lambda (x) x) x)) 1)"), 1)

    def test_bad_syntax(self):
        with self.assertRaises(SyntaxError):
            parse("1)")
        with self.assertRaises(SyntaxError):
            parse("1(")
        with self.assertRaises(SyntaxError):
            parse("(1")
        with self.assertRaises(Syntax
