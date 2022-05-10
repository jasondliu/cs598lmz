import sys, threading

def run():
    os.chdir(os.path.dirname(sys.argv[0]))
    sys.path.append(os.path.abspath('../../'))
    import pygst
    pygst.require('0.10')
    import gst
    import gobject

    gobject.threads_init()

    pipeline = gst.Pipeline('pipeline')
    src = gst.element_factory_make('videotestsrc', 'src')
    sink = gst.element_factory_make('xvimagesink', 'sink')
    pipeline.add(src, sink)
    src.link(sink)

    pipeline.set_state(gst.STATE_PLAYING)
    gtk.main()

threading.Thread(target=run).start()
</code>

