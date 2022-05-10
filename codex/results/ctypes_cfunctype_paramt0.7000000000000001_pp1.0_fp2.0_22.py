import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, #return type
                          ctypes.c_double, #first argument type
                          ctypes.c_double, #second argument type
                          ctypes.c_double, #third argument type
                          )

f = FUNTYPE(lambda x,a1,a2: a1*np.sin(a2*x))
def derive_mse(model, data, weights=None):
    """

    :param model:
    :param data:
    :param weights:
    :return:
    """
    if weights is None:
        weights = np.ones(len(data))

    residuals = data - model
    sse = np.sum(residuals**2*weights)

    return sse



def derive_jac_mse(func, data, weights=None):
    """ Derive the jacobian of the mse

    :param func:
    :param data:
    :param weights:
    :return:
    """
    if weights is None:
        weights = np.ones(len(data
