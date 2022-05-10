import threading
# Test threading daemon to get the Tkinter window back after closing the external program

p1_process = None


def start_p1():
    global p1_process
    print("Starting program...")
    p1_process = Popen("C:\\Users\\gavin\\source\\projects\\galaxy_hunters\\galaxy-hunters\\bin\\Release\\GalaxyHunters.exe")
    print("Launched program...")


def stop_p1():
    print("Waiting for program to exit...")
    p1_process.wait()
    print("Program exited...")


p1_thread = threading.Thread(target=stop_p1, daemon=True)
p1_thread.start()
start_p1()

</code>

