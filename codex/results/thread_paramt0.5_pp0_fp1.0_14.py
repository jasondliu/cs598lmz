import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
 
# This function will be called in a thread
def get_input(list):
    input()
    list.append(None)
 
# Create a list which we will modify in the thread
list = []
# Create a thread and feed him the get_input function with our list
thread = threading.Thread(target=get_input, args=(list,))
# Start the thread
thread.start()
 
# Wait for the user to press enter
while not list:
    time.sleep(0.1)
 
# The user has pressed enter, let's finish up
print('done')
</code>

