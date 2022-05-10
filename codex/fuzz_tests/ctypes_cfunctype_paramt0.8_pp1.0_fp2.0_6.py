import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

# http://stackoverflow.com/questions/37064286/pygobject-set-gsettings-when-key-is-changed
class GSettingsCb(GObject.Object):
    __gtype_name__ = 'GSettingsCb'
    def __init__(self, gsettings, callback):
        GObject.Object.__init__(self)
        self.callback = callback

        callback_function = FUNTYPE(self.gsettings_changed)
        self.id = gsettings.connect('changed', callback_function, None)

    def gsettings_changed(self, gsettings, key, user_data):
        self.callback()

# https://gist.github.com/krystien/f76625d58a0e7aec435c
class GStElementCb(GObject.Object):
    __gtype_name__ = 'GStElementCb'
    def __init__(self, gst_element, signal, callback):
       
