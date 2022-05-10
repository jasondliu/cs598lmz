import signal
# Test signal.setitimer and signal.getitimer
def handler(signum, frame):
    print('Received USBL data')
    signal.alarm(2)
    
def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL,2,0)
    while True:
        time.sleep(100)
        
        
    signal.setitimer(signal.ITIMER_REAL,0,0)

if __name__ == "__main__":
    main()



# Test USBLParser class
# Test get_data method
# Test get_bearing method
# Test get_altitude method

# Test get_average method
