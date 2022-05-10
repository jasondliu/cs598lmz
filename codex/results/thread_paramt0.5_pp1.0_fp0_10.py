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
class MagicEightBall(object):
    def __init__(self):
        self.answers = {0: 'It is certain',
                        1: 'It is decidedly so',
                        2: 'Without a doubt',
                        3: 'Yes, definitely',
                        4: 'You may rely on it',
                        5: 'As I see it, yes',
                        6: 'Most likely',
                        7
