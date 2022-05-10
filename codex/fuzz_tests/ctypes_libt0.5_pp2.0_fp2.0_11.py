import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("AIO Launcher")

# Get user input
print("AIO Launcher")
print("1. Install")
print("2. Update")
print("3. Start")
print("4. Uninstall")
print("5. Exit")
print("")
choice = input("Enter choice: ")

# Check if input is a number
if choice.isdigit():
	choice = int(choice)
else:
	print("")
	print("Invalid choice!")
	exit()

# Check if input is between 1 and 5
if choice < 1 or choice > 5:
	print("")
	print("Invalid choice!")
	exit()

# Check if input is 1
if choice == 1:
	# Check if AIO Launcher is already installed
	if os.path.isfile("AIO Launcher.exe"):
		print("")
		print("AIO Launcher is already installed!")
		exit()

	# Install AIO Launcher
	os.system("git clone https://github.com/Pokechu22/AIO
