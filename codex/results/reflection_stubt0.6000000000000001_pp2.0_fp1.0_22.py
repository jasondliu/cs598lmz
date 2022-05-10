fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
""")
        self.assertOutput(err="TypeError: 'generator' object is not callable\n")

    def test_call_code(self):
        self.run_test("""
fn = lambda: None
fn.__code__()
""")
        self.assertOutput(err="TypeError: 'code' object is not callable\n")

    @unittest.skipIf(platform.machine() == "s390x", "TODO: Investigate on s390x")
    def test_call_closure(self):
        self.run_test("""
fn = lambda: None
fn.__closure__()
""")
        self.assertOutput(err="TypeError: 'tuple' object is not callable\n")

    def test_call_builtin_code(self):
        self.run_test("""
x = len
x.__code__()
""")
        self.assertOutput(err="TypeError: 'code' object is not callable\n")

    def test_call_built
