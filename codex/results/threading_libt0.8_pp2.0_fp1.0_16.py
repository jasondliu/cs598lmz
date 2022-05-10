import threading
threading.stack_size(67108864)


def _query(self):
    """
    Query the server to determine connection status.
    :return: Status code of the query command
    """
    with self.srv_lock:
        try:
            response = self.srv.query()
        except Exception as e:
            if self.DEBUG:
                print("Server failed to respond to query:", e)
            return 0
        if self.DEBUG:
            print("Server responded with status code", response.status_code)
        return response.status_code


def _send_data(message, self):
    """
    Send data to server.
    :param message: Message to be sent to server
    :return: Status code of send_data command
    """
    with self.srv_lock:
        try:
            response = self.srv.send_data(message)
        except Exception as e:
            if self.DEBUG:
                print("Server failed to respond to send_data:", e)
            return 0
        if self.DEBUG:
            print
