import sys, threading

def run():
	global bOpen
	global Q
	global outPort
	global inPort
	global err_out
	global err
	global err_mutex
	global lineLenMax
	global lineLen
	global line
	global line_mutex
	global telnet_mutex
	global lineBuf
	global print_mutex
	print lineBuf.get('buffer', '/dev/null')
	if bOpen:
		if not Q.empty():
			data = Q.get()
			if data != None:
				if data[2]>=lineLenMax:
					line_mutex.acquire()
					lineLen = 0
					line = ''
					line_mutex.release()
					print_mutex.acquire()
					print '\n',
					print_mutex.release()
					telnet_mutex.acquire()
					inPort.write(data
