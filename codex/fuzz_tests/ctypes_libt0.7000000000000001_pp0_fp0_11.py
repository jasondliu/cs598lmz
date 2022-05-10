import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\joshu\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe", 0)

# SET WALLPAPER TO THE FOLLOWING FOLDER
# C:\Users\joshu\AppData\Local\Programs\Python\Python37-32\python.exe
</code>
However, when I run the script as administrator, my wallpaper doesn't change. I'm assuming it's because of the path. How do I change my wallpaper to the C:\Users\joshu\AppData\Local\Programs\Python\Python37-32\python.exe using the ctypes library or anything else?

