import threading
threading.stack_size(67108864)

def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def stringToIntArray(input):
    return json.loads(input)


def intArrayToString(input):
    return json.dumps(input)


def stringToStringArray(input):
    return json.loads(input)


def stringArrayToString(input):
    return json.dumps(input)


def intToIntArray(input):
    if input is None:
        input = 0
    return [input]


def intArrayToInt(input):
    if len(input) == 0:
        return None
    return input[0]


def intArrayToIntArray(input):
    return input


def intArrayToIntArray2D(input):
    return [input]


def intArrayToIntArray3D(input):
    return [[input]]


def intArrayToIntArray4D(
