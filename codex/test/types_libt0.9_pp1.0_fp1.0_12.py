import types
types.ClassType
class OldStyleClass:
    pass

# new-style: classes deriving directly or indirectly from object
class NewStyleClass(object):
    pass

# indicate a variable is a class
type(OldStyleClass)
# __main__.OldStyleClass
type(NewStyleClass)
# __main__.NewStyleClass

type(type)
# type
type(type(OldStyleClass))
# type


type(object)
