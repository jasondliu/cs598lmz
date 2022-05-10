import sys, threading

def run():
    print("Program started")
    # start up the CanOpenBridge node
    subprocess.run([
        "examples/CanOpenController/CanOpenController",
        "-c", "examples/CanOpenController/config/example_ds402_controller_301.yml",
        "-b", "pcan", "-d", "pcan",
    ])
    print("Program exited")

threading.Thread(target=run).start()

time.sleep(1)

# connect to the CanOpenBridge mapper and add can devices to the ds402 motor group
r = xmlrpc.client.ServerProxy("http://localhost:8000/RPC")

r.ds402_add('ds402_1', 0x201)
r.ds402_add('ds402_2', 0x202)
time.sleep(1)

# synchronously start the motors
print("Starting")

r.ds402_drive_operation['ds402_1'].start(1)
r.ds402_drive_operation['ds402_2'].start(1)
time.sleep(
