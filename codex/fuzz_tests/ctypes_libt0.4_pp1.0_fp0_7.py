import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# 파일 열기
file = open("C:/Users/user/Desktop/Python/Python_Basic/file/test.txt", 'w')
file.write("Life is too short")
file.close()

# 파일 읽기
file = open("C:/Users/user/Desktop/Python/Python_Basic/file/test.txt", 'r')
print(file.read())
file.close()

# 파일 쓰기
file = open("C:/Users/user/Desktop/Python/Python_Basic/file/test.txt", 'a')
file.write("You need python")
file.close()

# 파일 읽기
file = open("C:/Users/user/Desktop/Python/Python_Basic/file/test.txt", 'r')
print(file.read())
file.close()

# 파
