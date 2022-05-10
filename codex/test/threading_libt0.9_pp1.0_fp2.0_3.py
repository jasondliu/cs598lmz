import threading
threading.Thread(None, agent_msg_checker, args=(q,dQ,)).start()
threading.Thread(None, search_cmd_parser, args=(q,dQ,)).start()
threading.Thread(None, search_cmd_send, args=(dQ,dQ2,)).start()
threading.Thread(None, search_result_send, args=(dQ2,dQ,)).start()
threading.Thread(None, search_result_receiver, args=(q,dQ,)).start()                                                                                

while 1:                                                                                
    q.get()
