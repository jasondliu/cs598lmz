import threading
threading.stack_size(1024*1024*1024*8)

def create_source_file(device_name, device_ip, device_type):
    # Create the source file for the device
    with open(device_name, "w") as f:
        f.write("device_type = " + device_type + "\n")
        f.write("ip_address = " + device_ip + "\n")
        f.write("username = admin\n")
        f.write("password = admin\n")
        f.close()

# Create a device object
def create_device(device_name, device_ip, device_type):
    # Create the source file for the device
    create_source_file(device_name, device_ip, device_type)

    # Create the Netmiko connection object
    device = ConnectHandler.from_file(device_name)

    # Return the device object
    return device 

