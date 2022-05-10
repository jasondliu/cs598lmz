import mmap
import sys
import time

# global vars
last_message = ''
path = ''


def watch_file(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            try:
                while True:
                    line = f.readline()
                    if len(line) > 0:
                        yield line
                    else:
                        time.sleep(0.01)
            except KeyboardInterrupt:
                f.close()


def print_log(file):
    global path, last_message
    for line in watch_file(file):
        if path not in line:
            print(line.rstrip())
            last_message = line


def get_line_number(file):
    global last_message
    with open(file, 'r') as f:
        for num, line in enumerate(f, 1):
            if line == last_message:
                return num


