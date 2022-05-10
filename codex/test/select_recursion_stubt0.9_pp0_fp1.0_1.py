import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    def ensure_complains(f, *a):
        test_support.check_warnings(lambda: f(*a),
                                    _select.error,
                                    r"An attempt was made to select a fd.*\n",
                                    quiet=True)
        del a[:]

    ensure_complains(select.select, F(), [], [], [])
    ensure_complains(select.select, [F()], [], [], [])
    ensure_complains(select.select, [], [F()], [], [])
    ensure_complains(select.select, [], [], [F()], [])


class InstanceDispatcher:
    def __init__(self):
        self.functions = {}

    def register_function(self, obj, func):
        self.functions[obj] = func
        return func

    def unregister_function(self, obj):
        del self.functions[obj]

    def dispatch(self, obj):
        return self.functions[obj]()


