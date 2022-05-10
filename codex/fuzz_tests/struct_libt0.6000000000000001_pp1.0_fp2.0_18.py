import _struct
import time
import sys

# For each packet, print out the source IP address and the packet contents.

def print_packet(packet):
    print(packet[0], _struct.unpack('I', _struct.pack('I', packet[1])))

#for p in _sniff.sniff():
#    print_packet(p)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "replay":
            for p in _sniff.replay():
                print_packet(p)
        else:
            print("Usage: python3 sniff.py [replay]")
    else:
        while True:
            packet = _sniff.sniff()
            if packet:
                print_packet(packet)

if __name__ == "__main__":
    main()
