import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create window
window = Gtk.Window()
window.set_title("Test")
window.set_default_size(800, 600)

# Create a webview to show a website
webview = WebKit2.WebView()
webview.load_uri("https://github.com/baudtack/pywebkit2gtk")

# Add everything and initialize the window
window.add(webview)
window.show_all()

# Run everything
Gtk.main()
