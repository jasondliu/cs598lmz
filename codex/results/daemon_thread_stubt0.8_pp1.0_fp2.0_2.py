import sys, threading

def run():
    def task1():
        for i in range(10):
            print('1')
            yield
    def task2():
        for i in range(10):
            print('2')
            yield
    def task3():
        for i in range(10):
            print('3')
            yield
    tasks = [task1(), task2(), task3()]
    while tasks:
        task = tasks.pop(0)
        try:
            next(task)
            tasks.append(task)
        except StopIteration:
            pass

threading.Thread(target = run).start()

import sys, threading

def run():
    def task1():
        for i in range(10):
            print('1')
            yield
    def task2():
        for i in range(10):
            print('2')
            yield
    def task3():
        for i in range(10):
            print('3')
            yield
    tasks = [task1(), task2(), task3()]
    while tasks:
        task = tasks.pop(0
