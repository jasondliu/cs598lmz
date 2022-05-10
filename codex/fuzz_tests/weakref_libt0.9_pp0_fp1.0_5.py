import weakref
	
	class VideoWidget(gtk.DrawingArea):
		__gsignals__ = {
			"expose-event": "override"
		}
		def __init__(self):
			gtk.DrawingArea.__init__(self)
			self._video_window_xid = 0
			self.wscreen = None
			self.__dormant = False
			self.add_events(gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK)
			self.connect('realize', self._realize)
			self.connect('expose-event', self.expose)
		def set_dormant(self, dormant):
			self.__dormant = dormant
		def is_dormant(self):
			return self.__dormant
		def do_expose_event(
