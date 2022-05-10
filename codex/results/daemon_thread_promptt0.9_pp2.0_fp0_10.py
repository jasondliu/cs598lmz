import threading
# Test threading daemon
import time

def write_file_thread(file):
    with open(file, 'w') as f:
        print("write_file_thread:[{}]".format(threading.current_thread()))
        f.write("Hello world!\n")
        f.write("Bonjour monde!\n")
        f.write("!!@\n!!")

# time.strftime("%Y-%m")
# http://stackoverflow.com/questions/3874701/why-is-my-python-thread-not-exiting-after-i-call-join
t = threading.Thread(target=write_file_thread, args=("threadfile.txt",), daemon=True)
t.start()
time.sleep(10)
t.join()
# t.join()

print("Done ...")
