from types import FunctionType
list(FunctionType(lambda: (yield from), globals(), 'foo')())  # pass a test

import pickleable
# Pass a test:
type(pickleable.PickleableObjectWithNonpickleableInstance([])) is pickleable.PickleableObjectWithNonpickleableInstance
