import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("data.db")

# Found this at https://stackoverflow.com/questions/18283920/python-os-system-doesnt-return-until-program-exits
def run(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

# Found this at https://stackoverflow.com/questions/4690600/parse-json-in-python
def parse_json(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
    return data

# Found this at https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable
