import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello world\n")).start()

## 2: (Task 2) Make Two Chairs
class Chair(object):
    def __init__(self):
        self.legs = 5
        self.color = 'red'
        self.material = 'wood'
        
chair1 = Chair()
chair2 = Chair()

## 3: (Task 3) Create a table
class Table(object):
    def __init__(self):
        self.legs = 4
        self.color = 'brown'
        self.material = 'wood'
        
table = Table()

## 4: (Task 4) The other side of the Magic 8 Ball
