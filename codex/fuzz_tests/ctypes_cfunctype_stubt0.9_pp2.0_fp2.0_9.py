import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def cpy_phone():
    bpy.app.driver_namespace['phone'] = model.phone(fun)


def register():
    print("registerings")
    bpy.types.WindowManager.phone = bpy.props.PointerProperty(type=PhonePanel, name='Phone Panel')
    bpy.types.Scene.phone_props = bpy.props.CollectionProperty(type=PhoneItem)
    bpy.types.Scene.phone_index = bpy.props.IntProperty()


def unregister():
    print("unregisterings")
    del bpy.types.WindowManager.phone
    # del bpy.types.Scene.phone_index
    # del bpy.types.Scene.phone_index


if __name__ == "__main__":
    register()
