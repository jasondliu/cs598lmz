import sys, threading

def run():
    
    def m_if_event(event):
        global event_queue, m_if_started
        print('m_if: starting')
        time.sleep(4)
        print('m_if: Stopping')
        m_if_started = False
        event_queue.append(['m_if', 'stopped'])
        
    def m_of_event(event):
        global event_queue, m_of_started
        print('m_of: starting')
        time.sleep(6)
        print('m_of: Stopping')
        m_of_started = False
        event_queue.append(['m_of', 'stopped'])
        
    def m_op_event(event):
        global event_queue, m_op_started
        print('m_op: starting')
        time.sleep(8)
        print('m_op: Stopping')
        m_op_started = False
        event_queue.append(['m_op', 'stopped'])
        
    def m_io_event(event):
