import types
types.ClassType

class OldClass:
    pass

class NewClass(object):
    pass

print type(OldClass)
print type(NewClass)

print type(OldClass())
print type(NewClass())

print type(OldClass) == types.ClassType
print type(NewClass) == types.ClassType

print type(OldClass()) == types.InstanceType
print type(NewClass()) == types.InstanceType


# class Class:
#     pass
#
# print type(Class)
# print type(Class())
#
# print type(Class) == types.ClassType
# print type(Class()) == types.InstanceType
#
# print type(Class) == types.TypeType
# print type(Class()) == types.InstanceType
#
# print type(type)
# print type(type(Class))
#
# print type(type) == types.ClassType
# print type(type(Class)) == types.TypeType

# print type(type(type))
# print type(type(type(Class)))
#
# print type(type
