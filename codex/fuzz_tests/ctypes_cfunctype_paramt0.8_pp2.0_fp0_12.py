import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)


def udi_popup_dialog(popup_dict, title, message):
    """
    A generic "popup" dialog.

    Parameters
    ----------
    popup_dict : dict
        A dictionary of popup options.  (See ``UdiTypes``)

    title : str
        The string to be displayed as the title of the dialog.

    message : str
        The string to be displayed in the dialog.

    Returns:
        Returns a value from ``popup_dict``.

    Raises
    ------
    ValueError
        If ``popup_dict`` does not contain a key for all of the return values
        in ``UdiTypes.POPUP_RETURN``.
    """
    # TODO: move the check for missing types in the popup dictionary
    # to the internal C layer?
    #
    # Additionally, we only set up a function to handle the value that
    # is returned.  It would be more efficient to use a function that
    # returns an int, and then set up a switch
