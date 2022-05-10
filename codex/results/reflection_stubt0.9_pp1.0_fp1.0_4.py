fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi # type: ignore
fn() # pragma: no cover
def f(): # pragma: no cover
    while True:
        pass
f()
"""
        with self.assertRaises(RuntimeError) as ctx:
            mypy.check_multiple_files([f], mypy_params=mypy_params)
        self.assertIn("Coroutine 'f' was never awaited", ctx.exception.args[0])


class TestImports(unittest.TestCase):

    def check_module(self, module_path, find_modules=False, verbosity=0):
        assert verbosity in [0, 1, 2], "verbosity must be in {0, 1, 2}"
        if find_modules:
            # TODO: Get rid of the need for this special path.
            search_paths = [os.path.join(example_dir, 'package')]
        else:
            search_paths = None
        if verbosity >= 1:
            print('type checking %s...' % module_path)
        mypy.check_module
