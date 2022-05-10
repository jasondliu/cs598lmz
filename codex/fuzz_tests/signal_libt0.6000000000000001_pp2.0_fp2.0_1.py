import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def on_launch():
    if settings.get_setting('first_launch') == 'true':
        settings.set_setting('first_launch', 'false')
        settings.open_settings()

def on_exception(type, value, traceback):
    import traceback
    traceback.print_exception(type, value, traceback)

on_launch()
gobject.threads_init()
gobject.set_application_name(app_name)
gobject.set_prgname(app_name)
gobject.idle_add(on_launch)

# Set default icon
gtk.window_set_default_icon_from_file(paths.get_resource('img', 'icon.png'))

# Set exception hook
sys.excepthook = on_exception

# Set window size
gtk.gdk.screen_get_default().connect('size-changed', on_screen_size_changed)
gtk.settings_get
