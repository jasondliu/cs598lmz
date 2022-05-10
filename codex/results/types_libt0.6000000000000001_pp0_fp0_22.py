import types
types.MethodType(patch_method, test_class)

# patch_method(test_class)

test_class.test_method = patch_method
test_class.test_method()
