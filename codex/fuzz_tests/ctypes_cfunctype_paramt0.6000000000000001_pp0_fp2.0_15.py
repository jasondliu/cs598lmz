import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

def drag_force(position, velocity, drag_coefficient=1.0, reference_area=1.0, fluid_density=1.0, a=0.0, b=0.0, c=0.0):
    '''
    Calculates the drag force.

    Parameters
    ----------
    position : np.ndarray
        The 3D position of the object in the frame of reference
    velocity : np.ndarray
        The 3D velocity of the object in the frame of reference
    drag_coefficient : float
        The drag coefficient.
    reference_area : float
        The reference area of the object.
    fluid_density : float
        The density of the fluid.

    Returns
    -------
    np.ndarray
        The drag force of the object.
    '''
    return -drag_coefficient * reference_
