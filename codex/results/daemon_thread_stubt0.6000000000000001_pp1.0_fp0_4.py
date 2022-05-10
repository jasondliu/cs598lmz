import sys, threading

def run():
	sys.path.append('/usr/local/lib/python2.7/site-packages')
	import cv2
	#import numpy as np
	global img
	global run_thread
	global capture
	capture = cv2.VideoCapture(0)
	#while True:
	while run_thread:
		ret, img = capture.read()
		#cv2.imshow('asd',img)
		#cv2.waitKey(30)

def get_img():
	global img
	return img

def start():
	global run_thread
	run_thread = True
	thread = threading.Thread(target=run)
	thread.start()

def stop():
	global run_thread
	run_thread = False
