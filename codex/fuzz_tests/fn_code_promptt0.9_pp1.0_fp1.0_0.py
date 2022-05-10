fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = (
    "firstArgument", "thirdArgument", "secondArgument")

prop_recorder = []
try:
    with VarPrinter(test_fn, custom_prop_printer=lambda self, prop,
                                                 value: prop_recorder.append(prop)):

        print("This will be printed before the property names...")

        # All the following object accesses will call the lambda,
        # which will record the accessed property in prop_recorder.
        test_fn.firstArgument
        test_fn.does_not_exist
        test_fn.secondArgument
        test_fn.whatever
        test_fn.thirdArgument
except Exception:
    pass
print("Printed property names:")
for prop_name in prop_recorder:
    print(prop_name)
