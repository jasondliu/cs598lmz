import types
types.MethodType(throwing_type_error, None)

# these are not errors
import types
types.MethodType(throwing_type_error, throwing_type_error)

# these are not errors
import types
types.MethodType(throwing_type_error, throwing_value_error)

# these are not errors
import types
types.MethodType(throwing_value_error, throwing_type_error)

# these are not errors
import types
types.MethodType(throwing_value_error, throwing_value_error)

# these are not errors
import types
types.MethodType(throwing_value_error, throwing_value_error, throwing_type_error)

# these are not errors
import types
types.MethodType(throwing_value_error, throwing_value_error, throwing_value_error)

# these are not errors
import types
types.MethodType(throwing_value_error, throwing_value_error, throwing_value_error, throwing_type_error)

# these are not errors
import types
types.MethodType(
