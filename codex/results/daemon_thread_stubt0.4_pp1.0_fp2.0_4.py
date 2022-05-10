import sys, threading

def run():
    print("Hello from new thread")

thread = threading.Thread(target=run)
thread.start()

print("Hello from main thread")

# Wait for the thread to complete before exiting the program
thread.join()

print("Program completed")

#
#
# from threading import Thread
#
# def run():
#     print("Hello from new thread")
#
# thread = Thread(target=run)
# thread.start()
#
# print("Hello from main thread")
#
# # Wait for the thread to complete before exiting the program
# thread.join()
#
# print("Program completed")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

