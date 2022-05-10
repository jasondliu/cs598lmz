import threading
threading.stack_size(67108864) 

import server
import input
import output

if __name__ == "__main__":
	thread1 = threading.Thread(target = input.do_send, args = (server.server,))
	thread1.start()
	thread2 = threading.Thread(target = server.do_listen, args = (input.input_socket, output.output_socket,))
	thread2.start()
	thread3 = threading.Thread(target = output.do_recv, args = ())
	thread3.start()
