import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

def main():
	if (len(sys.argv) > 1):
		path = sys.argv[1]
		print(path)
	else:
		print("you need to indicate the path to the directory that contains the videos")
		return -1

	if not os.path.isdir(path):
		print("there is no directory in the path you provided")
		return -1

	files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

	for f in files:
		name, ext = os.path.splitext(f)
		if ext == ".mp4":
			print(f)
			video_path = path + "/" + f
			command = "ffmpeg -i " + video_path + " -r 30 -vf scale=320:240 -f image2 -qscale:
