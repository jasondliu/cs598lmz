import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# from https://github.com/jupyterlab/jupyterlab/issues/2227
def _jupyter_server_extension_paths():
    return [{
        'module': 'jupyterlab_git',
    }]

# from https://github.com/jupyterlab/jupyterlab/issues/2227
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="jupyterlab_git",
        # _also_ in the `nbextension/` namespace
        require="jupyterlab_git/extension")]
