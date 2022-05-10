import sys, threading

def run():
	os.system("powershell.exe -ExecutionPolicy ByPass -File resolver.ps1")
	

def main():
	time.sleep(1)
	os.system("color 0a")
	os.system("cls")
	print("    ____  __            _____             _ ")
	print("   / __ \/ /____  _____/ ___/__________  (_)____")
	print("  / /_/ / __/ _ \/ ___/\__ \/ ___/ ___/ / / ___/")
	print(" / ____/ /_/  __/ /   ___/ / /__/ /  / / (__  ) ")
	print("/_/    \__/\___/_/   /____/\___/_/  /_/_/____/  ")
	print("\n\n")
	print(Back.CYAN + Fore.BLACK + Style.BRIGHT + "Dns Resolver Tool")
	print("by " + Back.WHITE + Fore.BLACK + Style.BRIGHT + "Orloff~The
