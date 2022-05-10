import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Hacker's Toolbox")

# Initialise
print("Hacker's Toolbox")
print("Version: " + version)
print("Author: " + author)
print("")
time.sleep(2)

# Main Menu
def main():
    # Clear Console
    clear = lambda: os.system('cls')
    clear()

    # Print Menu
    print("Hacker's Toolbox")
    print("Version: " + version)
    print("Author: " + author)
    print("")
    print("1. Port Scanner")
    print("2. Password Generator")
    print("3. Password Cracker")
    print("4. Network Scanner")
    print("5. Website Scanner")
    print("6. Website Stealer")
    print("7. Website Defacer")
    print("8. Website Cloner")
    print("9. Website Crawler")
    print("10. Website Scraper")
    print("11. Website Spammer")
    print("12. Website Admin Finder")
    print("
