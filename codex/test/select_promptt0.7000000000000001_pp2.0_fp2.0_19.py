import select
# Test select.select()

import select
# Test select.select()


def test_select():
    # Test the use of epoll with select.select()
    # Create an epoll object
    epoll_fd = select.epoll()
    # Assume there is a list of sockets called my_sockets
    # Create a list of epoll events
    epoll_events = []
    for sock in my_sockets:
        # Create an epoll event associated with this socket
        # and append it to the list of epoll events
        epoll_events.append(select.epoll_event(select.EPOLLIN, sock))
    # Register the epoll events
    for epoll_event in epoll_events:
        epoll_fd.register(epoll_event)
    # Wait on input on all the epoll events and then
    # retrieve the list of events that are ready
    ready_epoll_events = select.epoll.select(epoll_events, [], [], 1)
