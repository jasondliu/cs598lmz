import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)


# 'Test_debugger'
##>>> transport.get_interaction_stream().sink.writer.writer.set_write_eof_matcher(
#                        Noémie dans toute sa splendeur
#pfft()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 8080))
clientsocket.settimeout(2)

print("Connection to server on port 8080")

f = clientsocket.makefile()
transport = InteractiveGdbTransport(f)
report_interaction = InteractiveGdbInteraction(transport.get_interaction_stream())
# transport.get_interaction_stream().sink.writer.write_eof = mock.Mock()
# transport.get_interaction_stream().sink.writer.write_eof = XMLRPCLogger(transport.get_interaction_stream().sink.
