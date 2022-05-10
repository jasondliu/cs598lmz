import sys, threading

def run():
    sys.stdout.write("\033[1;32m")
    sys.stdout.write("""




            """+"-"*30)
    sys.stdout.write("""
            \033[1;3;39m
                    _\n        /   \\\n       |     |\n    _  |     |  _\n | *| |     | |* |\n |_*_|     |_*_|\n""")
    sys.stdout.write("\033[1;34m"+"-"*30+"\n\n")
    sys.stdout.write("ZEROED !!!\n\n")
    sys.stdout.write("\033[1;32m")
    os.system("adb shell am start -n com.silentcircle.silentphone/.activities.ConfigurationActivity")
    time.sleep(4)
    os.system("adb shell input tap 53 142")
    time.sleep(1)
    os.system("adb shell input tap 55 444")
    time.sleep(
