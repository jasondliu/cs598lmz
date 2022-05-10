import socket
socket.if_indextoname(0)

_exit = exit
def exit(code):
  if code:
    print('FAILURE: self-tests failed!', file=sys.stderr)
  else:
    print('SUCCESS: self-tests passed!')
  _exit(code)


class RunMixin(object):

  def run(self, specific_join=False):
    self.threads = []

    tcp_server = threading.Thread(target=tcp_server_loop,
                                  args=(self.msg_queue,))
    self.threads.append(tcp_server)
    tcp_server.start()

    udp_server = threading.Thread(target=udp_server_loop,
                                  args=(self.msg_queue,))
    self.threads.append(udp_server)
    udp_server.start()

    main = threading.Thread(target=main_loop, args=(self.msg_queue, self))
    self.threads.append(main)
    main.start()

