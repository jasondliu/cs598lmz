import threading
# Test threading daemonic
start = time.time()
def takeANap():
    time.sleep(5)
    print('Wake up!')
threadObj = threading.Thread(target=takeANap)
threadObj.daemon = True
threadObj.start()
# main thread exits immediately after spawning new thread
print('End of program.')
end = time.time()
print(f'Program took {end - start} second(s) to execute.')
