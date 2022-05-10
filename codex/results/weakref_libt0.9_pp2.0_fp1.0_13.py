import weakref


def get_backend_list():
    """Get all the available audio device backends.

    Returns
    -------
    backends: list
        A list of audio device backend classes.

    Notes
    -----
    For the device to be truly available, the backend must be valid and
    working on the current system.  This is checked by calling
    the `is_available` method of each backend class.

    """
    sd_list = []
    backends = []
    backend_ids = []

    from .backend.win32 import WinBackend
    from .backend.jplayercore import JPlayerBackend

    for test_backend in (JPlayerBackend, WinBackend):
        if test_backend.is_available():
            sd_list.append(test_backend)
    for sd in sd_list:
        if sd.is_available():
            backends.append(sd)
            backend_ids.append(sd.get_backend_name())
    return backends, backend_ids


_sound_device_list, _sound_device
