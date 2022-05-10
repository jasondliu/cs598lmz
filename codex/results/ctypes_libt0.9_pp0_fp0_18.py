import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, data_folder + '\\'+'wallpaper.png' , 0)
pp = os.listdir(data_folder)

# Main loop
while True:
	##########################################################################
	# Directory
	dir_data = os.listdir(data_folder)
	# Sleep
	time.sleep(interval_asleep)
	# Directory
	dir_hup = os.listdir(data_folder)
	##########################################################################
	if len(dir_hup) != len(dir_data):
		# Directory
		dif_dir = [x for x in dir_hup if x not in dir_data]
		# Loop to convert every BMP to PNG
		for c in range(len(dif_dir)):
			# Change name
			photo = dif_dir[c]
			# Put photo in BG
			scr.grab().save(data_folder + '\\' + photo, "PNG")
			new =
