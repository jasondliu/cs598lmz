import sys, threading

def run():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from pytomo import Pytomo
    pytomo = Pytomo()
    pytomo.run()

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    if 'android' in sys.platform:
        import android
        android.map_key(android.KEYCODE_BACK, 1000)
        android.map_key(android.KEYCODE_MENU, 1001)
        android.map_key(android.KEYCODE_SEARCH, 1002)
        android.map_key(android.KEYCODE_CAMERA, 1003)
    elif 'darwin' in sys.platform:
        # mapping to F7, F8 and F9 keys
        import platform
        if 'Linux' in platform.system():
            import uinput
            events = (
                uinput.KEY_F7,
                uinput.KEY_F8,
