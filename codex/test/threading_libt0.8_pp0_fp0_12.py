import threading
threading.stack_size(67108864) 

# import every module in a different file
import calculator
import builder
import watch_folder

# Init threads
#calculator_thread = threading.Thread(target=calculator.start)
#calculator_thread.start()

builder_thread = threading.Thread(target=builder.start)
builder_thread.start()

watch_folder_thread = threading.Thread(target=watch_folder.start)
watch_folder_thread.start()
