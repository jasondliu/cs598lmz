gi = (i for i in ())
# Test gi.gi_code is None.
gi.gi_code = None
# Test gi.gi_frame is None
gi.gi_frame = None
# Test gi.gi_running is False
gi.gi_running = False

# class test_gen_1(unittest.TestCase):
#     # TODO: this test actually crashes python
#     # make sure not to run it
#     def test_crash_python(self):
#         code = """
#         def f():
#             yield 1
#             yield 2
#         """
#         exec(code)
#         a = f()
#         #print(a.gi_code)
#         exec(code, {'gi':a})
#         # this crashes python with a segfault


class test_gen_2(unittest.TestCase):
    def test_gi_code(self):
        import dis
        code = """
        def f():
            yield 1
            yield 2
        """
        exec(code)
        a = f()
        #print(a.gi_code)

