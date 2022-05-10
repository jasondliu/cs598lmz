import threading
# Test threading daemon

conn = sqlite3.connect('/home/pi/Desktop/TESTING/TESTING_DB.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS test(value REAL)')

def data_entry(value):
    c.execute("INSERT INTO test (value) VALUES(?)", (value,))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM test')
    data = c.fetchall()
    for row in data:
        print(row)

def main():
    create_table()
    data_entry(5)

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.
