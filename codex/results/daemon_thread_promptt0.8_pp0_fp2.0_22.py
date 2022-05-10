import threading
# Test threading daemon to see when it dies 
# https://stackoverflow.com/questions/8185346/pythons-threading-timer-does-not-work-as-expected-in-a-class-method
# https://stackoverflow.com/questions/38543506/threading-timer-not-working-in-python
# https://www.journaldev.com/15631/python-timer
class HouseTimer():
    def __init__(self):
        self.t = threading.Timer(5.0, self.handle_function)
    
    def handle_function(self):
        print('The timer has finished after 10 secs, self = {}'.format(self))
        print('The timer has finished after 10 secs, self.t.is_alive() = {}'.format(self.t.is_alive()))
        
    def start_timer(self):
        self.t.start()

    def state_of_timer(self):
        return self.t.is_alive()
        
    def cancel_timer(self):
       
