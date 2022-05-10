import sys, threading

def run():
    global last_line_num, last_line_str
    try:
        while True:
            line_str = sys.stdin.readline()
            if line_str == "":
                break
            last_line_num += 1
            last_line_str = line_str
    except:
        pass

def read_line():
    global last_line_num, last_line_str
    while True:
        if last_line_num != 0:
            line_str = last_line_str
            last_line_str = ""
            last_line_num = 0
            return line_str


thread = threading.Thread(target=run)
thread.start()

print("Start")

while True:
    line_str = read_line()
    if line_str == "":
        break
    print("Line: " + line_str)

thread.join()
