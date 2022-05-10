import types
types.ModuleType

# check code
# def check_code(self, code):
#     try:
#         self.assertMultiLineEqual(self.clean_lines(''.join(code)),
#             self.clean_lines(''.join(self.code)))
#     except (AssertionError, AttributeError):
#         raise Exception(self.code)

# _check = None
# def check_code(self, code):
#     global _check
#     _check = lambda: self.assertMultiLineEqual(self.clean_lines(''.join(code)),
#         self.clean_lines(''.join(self.code)))
#     return code

# def assertMultiLineEqual(self, first, second, msg=None):
#     first = str(first)
#     second = str(second)
#     if '\r\n' not in first and '\r\n' not in second:
#         self.assertEqual(first, second, msg)

# def get_lines(self, code):
#     raw = str(code)
