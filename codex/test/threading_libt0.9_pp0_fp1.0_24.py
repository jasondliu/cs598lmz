import threading
threading.stack_size(32768)


#import hds
#hds.FORDDOWNLOAD=False

import rtmp


def start(session, stream, **kwargs):
	video = VideoDevice(session, **kwargs)
	session.nav.playService(video)

	return video

