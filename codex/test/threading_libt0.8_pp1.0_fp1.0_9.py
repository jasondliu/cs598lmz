import threading
threading.active_count()

# Total number of threads
threading.enumerate()

# Name of the current thread
threading.current_thread()

#
threading.current_thread().getName()

###############################
###   THREADING FUNCTIONS
###############################

# Starting a thread
threading.Thread()


# Starting a thread using function

def function_to_be_executed(number):
    print("I am number {}".format(number))

my_thread = threading.Thread(target = function_to_be_executed, args = (1, ))
# target is a function that needs to be executed
# args is arguments to the function (in a tuple form)

my_thread.start()
print("This is the main thread {}".format(threading.current_thread().getName()))


# Starting a thread using class
class ClassName(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

