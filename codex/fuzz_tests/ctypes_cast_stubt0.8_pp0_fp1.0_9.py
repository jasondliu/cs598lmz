import ctypes
ctypes.cast(id(self), ctypes.py_object).value

i=0

class Callback:
    def __init__(self, l):
        self.lambda_fun = l

    def __call__(self, device, events):
        self.lambda_fun(device, events)


def func1(device, events):
    print("func1")
    print(device)
    print(events)
    print("\n")


def func2(device, events):
    print("func2")
    print(device)
    print(events)
    print("\n")


# 1-4: add and remove callbacks
print("1-4: add and remove callbacks")
gaze.subscribe_to(gaze.GAZE_DATA, Callback(func1))
gaze.subscribe_to(gaze.GAZE_DATA, Callback(func2))
gaze.unsubscribe_from(gaze.GAZE_DATA, Callback(func1))
gaze.wait_for(1000)

# 5-8: add and remove
