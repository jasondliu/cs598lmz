import sys, threading

def run():
    os.chdir("../")
    os.system("python3.7 main.py")

t = threading.Thread(target=run)
t.start()
time.sleep(1)
sys.exit()
</code>
Result:
console
Process finished with exit code -1073740791 (0xC0000409)
IDE
Process finished with exit code 0

