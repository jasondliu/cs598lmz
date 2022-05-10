import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
import time

# List of Producers

producer_name_list = []
no_of_producers = int(input("Enter the number of Producers : "))

for i in range(no_of_producers):
    producer_name_list.append("Producer "+str(i))

# List of Consumers

consumer_name_list = []
no_of_consumers = int(input("Enter the number of Consumers : "))

for i in range(no_of_consumers):
    consumer_name_list.append("Consumer "+str(i))

# Initializing the Buffer

buffer = Buffer(no_of_producers, no_of_consumers, producer_name_list, consumer_name_list)

# Initializing the Producers

producer_list = []
for i in range(no_of_producers):
    producer_list.append(Producer(buffer, i))

# Initializing the Consumers

consumer_list = []
for i in range(no_
