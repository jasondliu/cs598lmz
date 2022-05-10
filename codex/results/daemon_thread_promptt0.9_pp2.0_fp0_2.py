import threading
# Test threading daemon functionality
try:
    for i in range(2):
        process_thread = threading.Thread(target=spawn_process,args=('{} --file=f.mp3'.format('./mpv_py'),))
        process_thread.setDaemon(True)
        process_thread.start()
except Exception as e:
    print(e)
