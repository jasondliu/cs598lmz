import sys, threading

def run():
	#print "I am in run"
	while True:
		try:
			command = raw_input()
			if command == "show_devices":
				print "I am in show_devices"
			elif command == "show_ports":
				print "I am in show_ports"
			elif command == "show_connections":
				print "I am in show_connections"
			elif command == "create_device":
				print "I am in create_device"
			elif command == "remove_device":
				print "I am in remove_device"
			elif command == "create_connection":
				print "I am in create_connection"
			elif command == "remove_connection":
				print "I am in remove_connection"
			elif command == "exit":
				print "I am in exit"
				sys.exit()
			
