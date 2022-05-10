import sys, threading

def run():
	conf = {}
	with open('/home/pi/TFC-RPi/config/video_conf.json', 'r') as f:
		conf = json.load(f)
		
		# video recording
		if sys.argv[1] == 'start':	
			os.system(conf['video']['rec_command'])
		elif sys.argv[1] == 'stop':
			os.system('killall raspivid')
			
			# convert h264 to mp4
			try:
				if sys.argv[2]:
					# add date to filename
					date = dateutil.parser.parse(datetime.datetime.now().strftime('%H:%M:%S') + ' ' + sys.argv[2])
					infile  = conf['video']['rec_outfile'].replace('.mp4', '_%s.h264' % date.strftime('%H-
