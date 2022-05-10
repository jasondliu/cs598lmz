import types
types.ClassType
del types


new_java_class = None
JClass = None

try:
    # create a class based on the old_class template and add it to the given module
    def new_class(name, bases, dict, moduleName):
        new_class = new_java_class(name, bases, dict, moduleName)
        if moduleName:
            module = sys.modules.get(moduleName)
            if module is None:
                module = sys.modules[moduleName] = new.module(moduleName)
            setattr(module, name, new_class)
        return new_class

    def isJavaMethod(m):
        return hasattr(m, "im_self") and isinstance(m.im_self, JClass)

    def isJavaConstructor(m):
        return hasattr(m, "im_self") and is_instance_of(m.im_self, JClass)

    def isJavaClass(x):
        return hasattr(x, "_JAVA_CLASS_") and is_instance_of(x._JAVA
