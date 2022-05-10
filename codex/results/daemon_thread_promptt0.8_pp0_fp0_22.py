import threading
# Test threading daemon thread
# if you comment out the following setDaemon(True), the app will not terminate
# because the daemon thread is still alive
t = threading.Thread(target=lambda: sleep(10))
t.setDaemon(True)
t.start()


# Following code for testing threading's local data storage
# Test threading.local
class Student:
    _local = threading.local()
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._local.name

    def set_name(self, name):
        self._local.name = name


def student_thread(student, name):
    student.set_name(name)
    print(student.get_name())


s1 = Student("Tom")
s2 = Student("Jerry")

t1 = threading.Thread(target=student_thread, args=(s1, "Tommy"), daemon=True)
t2 = threading.Thread(target=student_thread, args=(s2, "Jerryy"), daemon=True)

