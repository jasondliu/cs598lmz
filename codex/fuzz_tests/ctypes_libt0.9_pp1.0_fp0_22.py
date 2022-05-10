import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

def isAdmin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    
print(isAdmin())
# os.path module

# os.path.basename(path) -> returns the final part of a path
# os.path.dirname(path) -> returns the directory path of a file

print('The file is ', os.path.basename(testFilePath))
print('The directory is ', os.path.dirname(testFilePath))
print('The absolute path is', os.path.abspath(testFilePath))
# os.path.exists(path) -> Returns True if a file exists
# os.path.isdir(path) -> Returns True if the path is a directory
# os.path.isfile(path) -> Returns True if the path is a file
# os.path.getsize(path) -> Returns the size of the file in bytes
# os.path.getatime(
