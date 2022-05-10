import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun!")
    return b"123"

mainloop = GLib.MainLoop()

if __name__ == "__main__":

    def on_change(proxy, sender_name, signal_name, parameters, user_data=None):
        print("CHANGE:", proxy, sender_name, signal_name, parameters, user_data)

    def on_connected(conn):
        print("connected")
        remote = Gio.DBusProxy.new_sync(conn, 
            Gio.DBusProxyFlags.NONE, None,
            'com.example.SampleService',
            '/com/example/SampleService/object',
            'com.example.SampleService.Type', None)
        print("remote:", remote)
        print("foo:", remote.get_cached_property('foo'))
        remote.connect('g-signal', on_change)
        remote.call_sync('HelloWorld', GLib.Variant("(i)", [12]), 0, -1, None)
        remote.call_sync('AddTwoNumbers', GL
