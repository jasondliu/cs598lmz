import types
# Test types.FunctionType is defined
try:
    types.FunctionType
except AttributeError:
    raise Exception("Required class not found: 'types.FunctionType'.")

from inspect import getmro
# Test inspect.getmro is defined
try:
    getmro
except NameError:
    raise Exception("Required function not found: 'inspect.getmro'.")

from inspect import isclass
# Test inspect.isclass is defined
try:
    isclass
except NameError:
    raise Exception("Required function not found: 'inspect.isclass'.")

from inspect import isfunction
# Test inspect.isfunction is defined
try:
    isfunction
except NameError:
    raise Exception("Required function not found: 'inspect.isfunction'.")

from inspect import ismodule
# Test inspect.ismodule is defined
try:
    ismodule
except NameError:
    raise Exception("Required function not found: 'inspect.ismodule'.")

from inspect import isroutine
# Test inspect.isroutine is defined
try:
    isroutine
except NameError:
