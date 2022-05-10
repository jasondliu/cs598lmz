import threading
threading.stack_size(32768)


#import hds
#hds.FORDDOWNLOAD=False

import rtmp


def start(session, stream, **kwargs):
	video = VideoDevice(session, **kwargs)
	session.nav.playService(video)

	return video

class VideoDevice:
	def __init__(self, session, **kwargs):
		print "videodevice init", kwargs
		self.session = session
		self.got_first_frame = None
		self.setStartTimes()

		self.stream = stream

		#self.stream.register_downstream_handler(self.service_handler)
		
		#self.stream.current_pcr = -1
		#self.stream.pcr_error_count = 0
		#self.stream.pcr_biterrors = 0
		#self.stream.abort = False

		self.event = [ None,
			self.pts_cycle_detected,
			self.
