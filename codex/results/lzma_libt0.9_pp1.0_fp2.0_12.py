import lzma
lzma.extractall(_XZ_CONV_PATH, Extract)

print(Fore.LIGHTGREEN_EX + "Extracted hostess config files successfully")
print(Fore.LIGHTGREEN_EX + "Checking system requirements")

# try:
#     import urllib.request
# except ImportError:
#     sys.exit(
#         "Failed: Python < 3.0 is not supported, please run this script with version Python3+")
#
# try:
#     import platform
#     if platform.system() != 'Darwin' and platform.system() != "Linux":
#         sys.exit(
#             "Failed: We only support Linux and macOS operating systems, sorry!")
# except ImportError:
#     print("Failed: Could not detect operating system, please report this issue")

# try:
#     from termcolor import colored
# except ImportError:
#     print(
#         "Failed: Please run " + Fore.RED + "pip3 install termcolor" + Fore.RESET + " before running this script")

if platform
