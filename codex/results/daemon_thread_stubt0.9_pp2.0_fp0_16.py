import sys, threading

def run():
    try:
        subprocess.run(
            ['python','main.py'],
            cwd = path,
            check = True
        )
    except subprocess.CalledProcessError:
        print("[DEBUG] subprocess finished with error code")

def check_file():
    try:
        subprocess.run(
            ['g++','main.cpp'],
            cwd = path,
            check = True
        )
    except subprocess.CalledProcessError:
        print("[DEBUG] C++ subprocess finished with error code")

def watch():
    modtime = None
    check_file()
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        time.sleep(1)
        try:
            modtime = os.stat(path+'main.py').st_mtime
            while True:
                if os.stat(path+'main.py').st_mtime > modtime:
                    modtime = os.stat(path+'main.py').st_mtime
                    check_
