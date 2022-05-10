import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

#CHANGED:
for x in range(1, 15):
    if x == 5:
        print("Task in progress...")
    time.sleep(1)

# This is now shown only after the loop is complete
print('Done')

# ORIGINAL:
print('Done')
for x in range(1, 15):
    if x == 5:
        print("Task in progress...")
    time.sleep(1)

# This is now shown only after the loop is complete
print('Done')
 
# OR:

# ORIGINAL:
print('Done')
for x in range(1, 15):
    if x == 5:
        print("Task in progress...")
    time.sleep(1)

# This is now shown only after the loop is complete
print('Done')

# OR:
for x in range(1, 15):
    if x == 5:
        print("Task in progress...")
    time.sleep(1)

# This is now shown only after the loop is
