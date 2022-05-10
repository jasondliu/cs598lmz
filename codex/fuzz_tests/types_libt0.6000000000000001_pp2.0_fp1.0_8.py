import types
types.MethodType(lambda self: None, None)
types.MethodType(lambda self, a: None, None)

# Bug 1350
from test.test_importhooks import TestImportHooks
TestImportHooks.test_import_package_from_nonpackage

# Bug 1351
from test import test_pkg
test_pkg.name

# Bug 1353
from test.test_importhooks import TestImportHooks
TestImportHooks.test_import_hook_succeeds_but_module_contains_errors

# Bug 1354
from test.test_importhooks import TestImportHooks
TestImportHooks.test_import_hook_with_failing_parent

# Bug 1355
from test.test_importhooks import TestImportHooks
TestImportHooks.test_import_hook_with_failing_parent_and_succeeding_child

# Bug 1356
from test.test_importhooks import TestImportHooks
TestImportHooks.test_import_hook_with_failing_parent_and_failing_child
