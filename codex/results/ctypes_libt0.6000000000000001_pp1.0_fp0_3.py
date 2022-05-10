import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Prints out all currently pressed keys
def get_pressed_keys(key):
	global key_list
	if key in key_list:
		key_list.remove(key)
	else:
		key_list.append(key)
	return key_list

# Takes in a list of characters that are currently pressed
# and returns a string of all the characters pressed
def convert_pressed_keys(key_list):
	pressed_keys = ''
	for i in key_list:
		pressed_keys += i
	return pressed_keys

# Listens for keyboard events
def on_press(key):
	global key_list, pressed_keys
	pressed_keys = convert_pressed_keys(key_list)
	if len(pressed_keys) > 0 and 'q' not in pressed_keys:
		print(pressed_keys)
		pressed_keys = ''
	else:
		print('Exiting...')
		listener.stop()
		sys.exit()


