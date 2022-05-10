import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Sopel - Exports")

export()
while 1:
	input("\nPress enter to re-export data.")
	export()
