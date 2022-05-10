import types
types.MethodType(f, None, class_test)
# class_test.f()
# class_test.__dict__
# class_test.__dict__['f']
# type(class_test)
# type(class_test.__dict__)
# type(class_test.__dict__['f'])

# type(class_test.f)
# class_test.f = MethodType(f, class_test, class_test.__class__)
# class_test.f()

# class_test.__dict__['f'] = MethodType(f, class_test, class_test.__class__)
# class_test.f()

# class_test.__dict__['f'] = f
# class_test.f()


# class_test.f()
# class_test.__dict__
# class_test.__class__
# class_test.__dict__['f']
# class_test.f = MethodType(f, class_test, class_test.__class__)
# class_test.f()


