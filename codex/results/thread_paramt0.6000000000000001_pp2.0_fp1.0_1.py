import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

from pprint import pprint

from netmiko import ConnectHandler

from my_devices import device_list

def output_printer(device_name, show_command):
    net_connect = ConnectHandler(**device_name)
    output = net_connect.send_command(show_command)
    print()
    print("#" * 80)
    print(device_name["ip"])
    print("#" * 80)
    print(output)
    print("#" * 80)
    print()

def main():
    for a_device in device_list:
        my_thread = threading.Thread(target=output_printer, args=(a_device, "show arp"))
        my_thread.start()

if __name__ == "__main__":
    main()
