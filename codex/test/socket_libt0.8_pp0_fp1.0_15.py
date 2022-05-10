import socket
import sys
import time

def get_data():

    data = []
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        data.append({"name": "Job", "nationality": "Prussian"})
        data.append({"name": "Moko", "nationality": "Nigerian"})
        data.append({"name": "Cholet", "nationality": "French"})
        data.append({"name": "Sobel", "nationality": "French"})
        data.append({"name": "Mussa", "nationality": "Egyptian"})
        data.append({"name": "Issa", "nationality": "Egyptian"})
        data.append({"name": "Farhan", "nationality": "Chinese"})
        data.append({"name": "Maulana", "nationality": "Indonesian"})
        data.append({"name": "Alaa", "nationality": "Egyptian"})
