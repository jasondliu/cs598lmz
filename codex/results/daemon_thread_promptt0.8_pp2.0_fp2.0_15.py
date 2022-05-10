import threading
# Test threading daemon
thread1 = threading.Thread(target=user_simulator.reset)
thread1.daemon = True
thread1.start()

print("Press enter to quit")
input()
user_simulator.stop()
print("Exiting")
