import types
types.ClassType

# The following doesn't work if the code above is executed
print type(Hello)

print type(Hello) == types.ClassType
print type(Hello()) == types.InstanceType
