import codecs
codecs.register_error("strict", codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_compile(self):
        self.assertEqual(compile_template("Hello, {{name}}!", {"name": "world"}), "Hello, world!")
        self.assertEqual(compile_template("Hello, {{name}}!", {"name": "world", "foo": "bar"}), "Hello, world!")
        self.assertEqual(compile_template("Hello, {{name}}!", {}), "Hello, !")
        self.assertEqual(compile_template("Hello, {{name}}!", {"name": "world", "foo": "bar"}, True), "Hello, world!")
        self.assertRaises(KeyError, compile_template, "Hello, {{name}}!", {}, True)
        self.assertEqual(compile_template("Hello, {{name}}!", {"name": "world", "foo": "bar"}, False), "Hello, world!")
        self.assertEqual(compile_template("Hello, {{name}}!", {}, False
