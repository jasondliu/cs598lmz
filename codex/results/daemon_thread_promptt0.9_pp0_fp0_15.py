import threading
# Test threading daemon
# Allow Ctrl-C to interrupt while thread is running
def start_interrupt_daemon_thread(interrupt_function=None, 
                                  num_loops=None):
    def interrupt_loop():
        halted = False
        num_loops = 0
        while not halted:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                print("Daemon: Keyboard Interrupt caught")
                if interrupt_function is not None:
                    interrupt_function()
                halted = True
            else:
                num_loops += 1
                print("Daemon: loop", num_loops)
                if (num_loops > 10):
                    halted = True
        # End while
        print("Daemon Thread exiting")  # pragma: no cover
        
    thread = threading.Thread(target=interrupt_loop)
    thread.daemon = True
    thread.start()                    # pragma: no cover


# Test without threading
def start_interrupt_test(interrupt_function=None, num_loops=None):
   
