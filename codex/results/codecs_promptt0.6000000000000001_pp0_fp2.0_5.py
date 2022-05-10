import codecs
# Test codecs.register_error('strict', codecs.replace_errors)

# from io import StringIO
# from contextlib import redirect_stdout

# def get_stdout(func):
#     f = StringIO()
#     with redirect_stdout(f):
#         func()
#     return f.getvalue()

# def test_get_stdout():
#     def print_hello():
#         print("hello")
#     assert get_stdout(print_hello) == "hello\n"

# class Test(unittest.TestCase):
#     def test_get_stdout(self):
#         def print_hello():
#             print("hello")
#         self.assertEqual(get_stdout(print_hello), "hello\n")

# if __name__ == '__main__':
#     unittest.main()
