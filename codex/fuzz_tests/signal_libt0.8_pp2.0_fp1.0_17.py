import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


def _(a, b, c):
    """
    Callback function for the detection of mouse buttons
    """
    if b == "PRESS" and a.name == "LEFTMOUSE":
        return {'RUNNING_MODAL'}
    elif b == "PRESS" and a.name == "ESC":
        return {"CANCELLED"}
    return {'PASS_THROUGH'}


def get_object_bbox(context, obj):
    """
    Compute the bounding box of the given object and return it
    in the format [[minx,miny,minz],[maxx,maxy,maxz]]
    """
    bb = []
    for i in [0, 1]:
        bpy.context.view_layer.objects.active = obj
        x, y, z = obj.matrix_world.to_translation()
        matrix = obj.matrix_world.copy()
        matrix_rot = matrix.to_3x3
