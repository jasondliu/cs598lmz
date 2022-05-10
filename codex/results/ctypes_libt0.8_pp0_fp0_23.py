import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("DanmakuGenerator")

danmakuFileName = input("Enter the .txt file name you have prepared: ")

# Enter the .txt file name you have prepared: example.txt
# Danmaku text: 弹幕文本
# Danmaku color: 颜色
# Danmaku size: 字号
# Danmaku duration: 持续时间
# Danmaku speed: 速度

fin = open(danmakuFileName, "r")
fout = open("danmakuList.csv", "w")

fout.write("text,color,size,duration,speed\n")

for line in fin:
    text = line.split(" ")[0]
    color = line.split(" ")[1]
    size = line.split(" ")[2]
    duration = line.split(" ")[3]
    speed = line.split(" ")[4]
    fout.write("%s,%s,
